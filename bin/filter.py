"""Check for assert statements in juptyer notebooks.

Without any flags, the script will check for assert statements only in code cells that produce
a visualisation. The search is not greedy by default. It will print the notebook to stdin if at
least 1 assert statement exists in the notebook.

With the `--proximity` flag, the script will also check in code cells directly below the
visualisation cells.

With the `--strict` flag, the script will only flag notebooks if the assert statements is in the
code cell below the visualisation cell. This flag takes precedence over `--proximity`.
"""

import json
import argparse
import pandas as pd
import numpy as np
from io import StringIO

pd.set_option("display.max_columns", 10)


def _list_to_str(x):
    return "".join(x)


def check(df: pd.DataFrame) -> bool:
    decision = (
        not df.empty and df["source"].apply(_list_to_str).str.contains("assert").any()
    )
    return decision


def get_cells(
    code_cells: pd.DataFrame,
    viz_cells: pd.DataFrame,
    strict: bool = False,
) -> pd.DataFrame:
    cells = []
    for idx, cell in viz_cells.iterrows():
        if not strict:
            # add cell with visualisation
            cells.append(cell)

        chunk = code_cells.loc[code_cells.index > idx]

        try:
            below = chunk.iloc[0]
        except IndexError:
            # chunk is empty or there were no code cells below the cell with visualistion
            # don't do anything
            pass
        else:
            cells.append(below)

    return pd.DataFrame(cells)


def filter(df: pd.DataFrame) -> pd.DataFrame:
    filtered = df.copy()
    if args.no_shape:
        filtered = filtered.loc[
            (filtered.source.str.contains("assert"))
            & ~(filtered.source.str.contains("shape"))
        ]

    if args.max_num_lines:
        filtered["source_num_lines"] = filtered.source.apply(lambda x: len(x))
        filtered = filtered.loc[(filtered.source_num_lines <= args.max_num_lines)]

    return filtered


def print_match() -> None:
    print(f"{args.notebook}")


def ipynb_to_dataframe() -> pd.DataFrame:
    frames = []

    with open(args.notebook) as f:
        cells = json.load(f)["cells"]
        df = pd.read_json(StringIO(json.dumps(cells)), orient="records")

        # early exit if empty notebook or no code cell in notebook
        if df.empty or df.loc[df["cell_type"] == "code"].empty:
            exit()

        # NOTE fill missing outputs with empty list
        # NOTE we have to iterate through them, cannot do a bulk assignment
        for idx, row in df.loc[df["outputs"].isna()].iterrows():
            df.at[idx, "outputs"] = []

        for row in df.itertuples():
            frame = {
                "index": [],
                "cell_type": [],
                "source": [],
                "image": [],
            }

            if len(row.outputs) == 0:
                frame["index"].append(row.Index)
                frame["cell_type"].append(row.cell_type)
                frame["source"].append(row.source)
                frame["image"].append(np.nan)
                frames.append(
                    pd.DataFrame(
                        data=frame,
                        index=frame["index"],
                        columns=["cell_type", "source", "image"],
                    )
                )
                continue

            for output in row.outputs:
                try:
                    frame["image"].append(output["data"]["image/png"])
                except KeyError:
                    frame["image"].append(np.nan)
                finally:
                    frame["index"].append(row.Index)
                    frame["cell_type"].append(row.cell_type)
                    frame["source"].append(row.source)

                frames.append(
                    pd.DataFrame(
                        data=frame,
                        index=frame["index"],
                        columns=["cell_type", "source", "image"],
                    )
                )

        return pd.concat(frames)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for assert statements in jupyter notebooks"
    )
    parser.add_argument(
        "notebook",
        help="Path to Jupyter Notebook",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--vis-cells",
        help="Check only in visualisation cells",
        action="store_true",
        default=False,
    )
    group.add_argument(
        "--proximity",
        help="Check in code cells below visualisation cells",
        action="store_true",
        default=False,
    )
    group.add_argument(
        "--strict",
        help="Check only in code cells below visualisation cells",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--no-shape",
        help="Exclude asserts that check shape",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--max-num-lines",
        help="Restrict max number of lines in the cell containing assert",
        type=int,
        default=None,
    )
    args = parser.parse_args()

    all_cells = ipynb_to_dataframe()
    code_cells = all_cells.loc[all_cells["cell_type"] == "code"]
    viz_cells = all_cells.loc[all_cells["image"].notna()]

    no_ml_lib = not (
        # NOTE after wrapping the json in StringIO, contains_ml_lib returns False even when the pattern
        # should match. So I am mapping the source column through a lambda function that joins list of
        # strings into a single string.
        code_cells["source"]
        .apply(_list_to_str)
        .str.contains(r"pandas|numpy|scipy|sklearn|torch|dask|tensorflow")
        .any()
    )

    no_code_cells = code_cells.empty
    no_viz_cells = viz_cells.empty

    if no_code_cells or no_ml_lib or no_viz_cells:
        # early exit if:
        # notebook does not contain any code cells or
        # the notebook is not ML/DS related or
        # notebook does not contain any visualisations
        exit()

    if not args.vis_cells and not args.proximity and not args.strict:
        cells = code_cells
    elif args.vis_cells:
        cells = viz_cells
    elif args.proximity:
        cells = get_cells(code_cells, viz_cells)
    elif args.strict:
        cells = get_cells(code_cells, viz_cells, strict=True)
    else:
        print("DEBUG:something went horribly wrong!")
        exit()

    not cells.empty and check(filter(cells)) and print_match()
