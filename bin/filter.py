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
import ast
import argparse
import pandas as pd
import numpy as np
from io import StringIO

pd.set_option("display.max_columns", 10)


def check(df: pd.DataFrame) -> bool:
    decision = (
            not df.empty and
            df["source"].apply(lambda x: "".join(x)).str.contains("assert").any()
            )
    return decision


def get_proximity_cells(
    all_cells: pd.DataFrame,
    viz_cells: pd.DataFrame,
    strict: bool = False,
) -> pd.DataFrame:
    cells = []
    for idx, cell in viz_cells.iterrows():
        if not strict:
            # add cell with visualisation
            cells.append(cell)

        chunk = all_cells.loc[all_cells.index > idx]

        try:
            below = chunk.loc[(chunk.cell_type == "code")].iloc[0]
        except IndexError:
            # chunk is empty or there were no code cells below the cell with visualistion
            # don't do anything
            pass
        else:
            cells.append(below)

    return pd.DataFrame(cells)


def filter(df: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
    filtered = df.copy()
    if args.no_shape:
        filtered = filtered.loc[
            (filtered.source.str.contains("assert"))
            & ~(filtered.source.str.contains("shape"))
        ]

    if args.max_num_lines:
        filtered["source_num_lines"] = filtered.source.apply(
            lambda x: len(x)
            )
        filtered = filtered.loc[(filtered.source_num_lines <= args.max_num_lines)]

    return filtered


def print_match() -> None:
    print(f'{args.notebook}')


def ipynb_to_dataframe(file: str) -> pd.DataFrame:
    frames = []

    with open(file) as f:
        cells = json.load(f)['cells']
        df = pd.read_json(StringIO(json.dumps(cells)), orient="records")

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
                frames.append(pd.DataFrame(
                    data=frame,
                    index=frame["index"],
                    columns=["cell_type", "source", "image"]
                    ))
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

                frames.append(pd.DataFrame(
                    data=frame,
                    index=frame["index"],
                    columns=["cell_type", "source", "image"]
                    ))

        return pd.concat(frames)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for assert statements in jupyter notebooks"
    )
    parser.add_argument(
        "notebook",
        help="Path to Jupyter Notebook",
    )
    parser.add_argument(
        "--no-shape",
        help="Exclude asserts that check shape",
        action="store_true",
        default=False,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--proximity",
        help="Include code cells below visualisation cells",
        action="store_true",
        default=False,
    )
    group.add_argument(
        "--strict",
        help="Check only in cells below visualisation cells",
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

    all_cells = ipynb_to_dataframe(args.notebook)

    contains_ml_lib = (
        # NOTE after wrapping the json in StringIO, contains_ml_lib returns False even when the pattern
        # should match. So I am mapping the source column through a lambda function that joins list of
        # strings into a single string.
        all_cells["source"]
        .apply(lambda x: "".join(x))
        .str.contains(r"pandas|numpy|scipy|sklearn|torch|dask|tensorflow")
        .any()
    )

    viz_cells = all_cells.loc[all_cells["image"].notna()]

    if not contains_ml_lib or viz_cells.empty:
        # early exit if the notebook is not ML/DS related
        # or does not contain any visualisations
        exit()
    elif not args.proximity and not args.strict:
        cells = viz_cells
    elif args.proximity:
        cells = get_proximity_cells(all_cells, viz_cells)
    elif args.strict:
        cells = get_proximity_cells(all_cells, viz_cells, strict=True)
    else:
        print("DEBUG:something went horribly wrong!")
        exit()
    not cells.empty and check(filter(cells, args)) and print_match()
