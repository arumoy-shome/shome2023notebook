"""Check for assert statements in juptyer notebooks.

Without any flags, the script will check for assert statements only in code cells that produce
a visualisation. The search is not greedy by default. It will print the notebook to stdin if at
least 1 assert statement exists in the notebook.

With the `--proximity` flag, the script will also check in code cells directly below the
visualisation cells.

With the `--strict` flag, the script will only flag notebooks if the assert statements is in the
code cell below the visualisation cell. This flag takes precedence over `--proximity`.
"""

import argparse
import pandas as pd
pd.set_option("display.max_columns", 10)


def check(df: pd.DataFrame) -> bool:
    return not df.empty and df["source"].str.contains("assert").any()


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

        # current cell & all cells below it; we cannot use idx+1 since we may be at the bottom edge
        chunk = all_cells.iloc[idx:]

        if not len(chunk) == 1:
            # we are not at the bottom edge, we should have at least 1 cell below the cell with
            # visualisation
            try:
                below = chunk.loc[
                    (chunk.cell_type == "code") &
                    (chunk.index != idx)
                ].iloc[0]
            except IndexError:
                # there were no code cells below the cell with visualistion; don't do anything
                pass
            else:
                cells.append(below)

    return pd.DataFrame(cells)


def print_match() -> None:
    print(f'{args.csv.replace("csv", "ipynb")}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for assert statements in jupyter notebooks"
    )
    parser.add_argument(
        "csv",
        help="Path to csv file",
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
    args = parser.parse_args()

    all_cells = pd.read_csv(args.csv, index_col=0)

    contains_ml_lib = all_cells["source"].str.contains(
        r"pandas|numpy|scipy|sklearn|torch|dask|tensorflow").any()

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

    check(cells) and print_match()
