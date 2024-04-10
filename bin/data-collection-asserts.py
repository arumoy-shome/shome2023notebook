"""Compute various statistics about Python assert statements in Jupyter Notebooks.
"""

import json
import argparse
import pandas as pd
import numpy as np
from io import StringIO
import os


def ipynb_to_dataframe() -> pd.DataFrame:

    with open(args.notebook) as f:
        cells = json.load(f)["cells"]
        df = pd.read_json(StringIO(json.dumps(cells)), orient="records")

    # NOTE: early exit if empty notebook or no code cells
    (df.empty or df.loc[df["cell_type"] == "code"].empty) and exit()

    # NOTE: remove empty cells
    # These can be of three types: NaN (float) "" (str) or [] (list)
    df = df.loc[df["source"].notna()]  # handle NaN
    df = df.loc[
        df["source"].apply(lambda x: True if x else False)
    ]  # handle empty "" or []

    # NOTE: convert `source` to str dtype
    # NOTE: `source` can be str or list; following lambda function works on both cases
    df.loc[:, "source"] = df["source"].apply(lambda x: "".join(x))

    return df.loc[:, ["cell_type", "source"]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute various statistics about Python assert statements in Jupyter Notebooks"
    )
    parser.add_argument(
        "notebook",
        help="Path to Jupyter Notebook",
    )
    args = parser.parse_args()
    print(f"INPUT:{args.notebook}")

    all_cells = ipynb_to_dataframe()
    code_cells = all_cells.loc[all_cells["cell_type"] == "code"]
    md_cells = all_cells.loc[all_cells["cell_type"] == "markdown"]

    import_cells = code_cells.loc[code_cells["source"].str.contains("import")]
    (
        import_cells.empty
        or import_cells.loc[
            import_cells["source"].str.contains(
                r"sklearn|torch|tensorflow|keras", regex=True
            )
        ].empty
    ) and exit()

    # NOTE: this may return false positives (such as the keyword `assert` appearing in a comment)
    assert_cells = code_cells.loc[code_cells["source"].str.contains("assert")]
    # NOTE: early exit if we don't have any code cells with `assert`
    assert_cells.empty and exit()

    # populate assert_content & assert_context
    assert_content = []
    assert_context = []
    for idx, cell in assert_cells.iterrows():
        cell["notebook"] = args.notebook
        assert_content.append(cell)
        # populate assert_context
        try:
            above = all_cells.loc[idx - 1]
        except KeyError:
            pass
        else:
            above["notebook"] = args.notebook
            above["location"] = "above"
            above["assert_cell_index"] = idx
            assert_context.append(above)

        try:
            below = all_cells.loc[idx + 1]
        except KeyError:
            pass
        else:
            below["notebook"] = args.notebook
            below["location"] = "below"
            below["assert_cell_index"] = idx
            assert_context.append(below)

    # NOTE: make sure that the term `ipynb` only occurs at the end of filename
    # I did this using the following command and checking that it *does not* print anything:
    # $ find data/ -name '*.ipynb' -type f -not -path '*ipynb_checkpoints*' |grep -v 'ipynb$'
    dirname, filename = os.path.split(args.notebook)
    dirname = dirname.replace("data/", "data/shome2023notebook/", 1)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    name = os.path.join(dirname, os.path.splitext(filename)[0])
    stats = {
        "notebook": args.notebook,
        "num_code_cells": len(code_cells),
        "num_md_cells": len(md_cells),
        "num_assert_cells": len(assert_cells),
    }
    # NOTE: order of headers ["notebook", "num_code_cells", "num_md_cells", "num_assert_cells"]
    pd.DataFrame(data=[stats]).to_csv(name + "-stats.csv", index=False, header=False)
    print(f"OUTPUT:{name}" + "-stats.csv")

    # NOTE: order of headers ["index", "cell_type", "source", "notebook"]
    pd.DataFrame(data=assert_content).to_csv(name + "-assert-content.csv", header=False)
    print(f"OUTPUT:{name}" + "-assert-content.csv")

    # NOTE: order of headers ["index", "cell_type", "source", "notebook", "location", "assert_cell_index"]
    pd.DataFrame(data=assert_context).to_csv(name + "-assert-context.csv", header=False)
    print(f"OUTPUT:{name}" + "-assert-context.csv")
