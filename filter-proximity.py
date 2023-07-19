"""Check for assert statements in proximity of visualisation cells."""

import argparse
import pandas as pd
pd.set_option("display.max_columns", 10)


def print_match():
    print(f'{args.csv.replace("csv", "ipynb")}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv",
        help="Path to csv file",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.csv, index_col=0)

    contains_ml_lib = df["source"].str.contains(
        r"pandas|numpy|scipy|sklearn|torch|dask|tensorflow").any()

    rows = df.loc[df["image"].notna()]

    if not contains_ml_lib or rows.empty:
        exit()

    series = []
    for idx, row in rows.iterrows():
        # add the current row with visualisation & assert statement
        series.append(row)

        # current row & all rows below it; we cannot use idx+1 since
        # we may be at the bottom edge
        chunk = df.iloc[idx:]
        if not len(chunk) == 1:
            # we are not at the bottom edge, we should have at least
            # 1 row below
            try:
                below = chunk.loc[
                    (chunk.cell_type == "code") &
                    (chunk.index != idx)
                ].iloc[0]
            except IndexError:
                # do nothing
                pass
            else:
                series.append(below)

    rows = pd.DataFrame(series)

    contains_assert = rows["source"].str.contains("assert").any()

    if contains_assert:
        print_match()
