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

    (df.empty or df.loc[df["cell_type"] == "code"].empty) and exit()

    # NOTE: remove cells with no outputs
    # These can be of two type: NaN (float) or [] (list)
    df = df.loc[df["outputs"].notna()]  # handle NaN
    df = df.loc[df["outputs"].apply(lambda x: True if x else False)]  # handle empty []

    # for idx, row in df.loc[df["outputs"].isna()].iterrows():
    # df.at[idx, "outputs"] = []

    # NOTE: early exit if no outputs
    df.empty and exit()

    df.loc[:, "source"] = df["source"].apply(lambda x: "".join(x))

    return df.loc[:, ["cell_type", "source", "outputs"]]


def get_outputs():
    rows = []

    for idx, cell in code_cells.iterrows():
        for output in cell.outputs:
            frame = {
                "notebook": args.notebook,
                "index": idx,
                "source": cell.source,
                "output_type": output["output_type"],
                "text": None,
                "image": None,
                "has_html": None,
            }

            if (output["output_type"] == "stream" and output["name"] == "stdout"):
                frame["text"] = output["text"]

            if output["output_type"] in ["display_data", "execute_result"]:
                try:
                    frame["image"] = output["data"]["image/png"]
                except KeyError:
                    pass

                try:
                    frame["text"] = output["data"]["text/plain"]
                except KeyError:
                    pass

                try:
                    frame["has_html"] = len(output["data"]["text/html"]) != 0
                except KeyError:
                    pass

            rows.append(frame)

    if rows:
        _indices = [v for row in rows for k, v in row.items() if k == "index"]
        rows = pd.DataFrame(data=rows, index=_indices).drop(columns="index")
        rows = rows.loc[rows["image"].notna() | rows["text"].notna()]
        rows.loc[:, "text"] = rows.loc[:, "text"].apply(lambda x: "".join(x))
    else:
        rows = pd.DataFrame()

    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "notebook",
    )
    args = parser.parse_args()
    print(f"INPUT:{args.notebook}")

    all_cells = ipynb_to_dataframe()
    code_cells = all_cells.loc[all_cells["cell_type"] == "code"]

    import_cells = code_cells.loc[code_cells["source"].str.contains("import")]
    (
        import_cells.empty
        or import_cells.loc[
            import_cells["source"].str.contains(
                r"sklearn|torch|tensorflow|keras", regex=True
            )
        ].empty
    ) and exit()

    outputs = get_outputs()
    # NOTE: early exit if neither outputs.data.{"image/png","text/plain"} were present
    outputs.empty and exit()

    dirname, filename = os.path.split(args.notebook)
    dirname = dirname.replace("data/", "data/shome2023notebook/", 1)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # NOTE: order of headers ["index", "notebook", "source", "image/png", "text/plain"]
    name = os.path.join(dirname, os.path.splitext(filename)[0] + "-outputs.csv")
    outputs.to_csv(name, header=False)
    print(f"OUTPUT:{name}")
