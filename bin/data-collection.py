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

    # NOTE: fill missing outputs with empty list
    # NOTE: we have to iterate through them, cannot do a bulk assignment
    for idx, row in df.loc[df["outputs"].isna()].iterrows():
        df.at[idx, "outputs"] = []

    # NOTE: remove empty cells
    # These can be of three types: NaN (float) "" (str) or [] (list)
    df = df.loc[df["source"].notna()]  # handle NaN
    df = df.loc[
        df["source"].apply(lambda x: True if x else False)
    ]  # handle empty "" or []

    # NOTE: convert `source` to str dtype
    # NOTE: `source` can be str or list; following lambda function works on both cases
    df.loc[:, "source"] = df["source"].apply(lambda x: "".join(x))

    return df.loc[:, ["cell_type", "source", "outputs"]]


def _has_vis(outputs):
    if len(outputs) == 0:
        return False

    results = []
    for output in outputs:
        result = "data" in output.keys() and "image/png" in output["data"].keys()
        results.append(result)

    return True in results


def get_visualisations():
    cells = []

    for idx, cell in all_cells.loc[all_cells["outputs"].apply(_has_vis)].iterrows():
        for output in cell.outputs:
            # NOTE: (refactor) ideally get_visualisations should not have to check this, it should just operate with the assumption that output["data"]["image/png"] exists
            if "data" in output.keys() and "image/png" in output["data"].keys():
                frame = {}
                frame["notebook"] = args.notebook
                frame["index"] = idx
                frame["image/png"] = output["data"]["image/png"]

                cells.append(frame)

    indices = [v for cell in cells for k, v in cell.items() if k == "index"]
    return pd.DataFrame(data=cells, index=indices).drop(columns="index")


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

    if code_cells.loc[code_cells["outputs"].apply(_has_vis)].any().any():
        visualisations = get_visualisations()
    else:
        visualisations = pd.DataFrame()

    # NOTE: remove outputs column
    all_cells = all_cells.loc[:, ["cell_type", "source"]]
    code_cells = code_cells.loc[:, ["cell_type", "source"]]

    md_cells = all_cells.loc[all_cells["cell_type"] == "markdown"]

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
    basename, _ = os.path.splitext(args.notebook)
    dirname = os.path.dirname(args.notebook).replace(
        "data/", "data/shome2023notebook/", 1
    )
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    stats = {
        "notebook": args.notebook,
        "num_code_cells": len(code_cells),
        "num_md_cells": len(md_cells),
        "num_assert_cells": len(assert_cells),
    }
    # NOTE: order of headers ["notebook", "num_code_cells", "num_md_cells", "num_assert_cells"]
    pd.DataFrame(data=[stats]).to_csv(
        basename + "-stats.csv", index=False, header=False
    )
    print(f"OUTPUT:{basename}" + "-stats.csv")
    # NOTE: order of headers ["index", "cell_type", "source", "notebook"]
    pd.DataFrame(data=assert_content).to_csv(
        basename + "-assert-content.csv", header=False
    )
    print(f"OUTPUT:{basename}" + "-assert-content.csv")
    # NOTE: order of headers ["index", "cell_type", "source", "notebook", "location", "assert_cell_index"]
    pd.DataFrame(data=assert_context).to_csv(
        basename + "-assert-context.csv", header=False
    )
    # NOTE: order of headers ["index", "notebook", "image/png"]
    print(f"OUTPUT:{basename}" + "-assert-context.csv")
    if not visualisations.empty:
        visualisations.to_csv(basename + "-visualisations.csv", header=False)
        print(f"OUTPUT:{basename}" + "-visualisations.csv")
