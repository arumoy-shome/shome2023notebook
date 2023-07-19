"""Filter the csv files with images and assert statement(s)."""

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
    parser.add_argument(
        "--check-assert",
        action="store_true",
        help="Check presence of assert statement",
    )
    parser.add_argument(
        "--check-ml-lib",
        action="store_true",
        help="Check presence of popular ML libraries",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.csv, index_col=0)
    rows = df.loc[df["image"].notna()]

    contains_assert = rows["source"].str.contains("assert").any()
    contains_ml_lib = rows["source"].str.contains(
        r"pandas|numpy|scipy|sklearn|torch|dask|tensorflow").any()
    # TODO implement this search: we need to isolate md cells and
    # match in there
    # contains_markdown = ???

    if args.check_assert and contains_assert:
        print_match()
    elif args.check_ml_lib and contains_ml_lib:
        print_match()
    else:
        if contains_assert and contains_ml_lib:
            print_match()
