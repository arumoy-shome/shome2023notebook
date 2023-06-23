import argparse
import json
import numpy as np
import pandas as pd
pd.set_option("display.max_columns", 10)

if __name__ == "__main__":
    frames = []

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "notebook",
        help="Path to Jupyter Notebook",
    )
    args = parser.parse_args()

    with open(args.notebook) as f:
        cells = json.load(f)['cells']
        df = pd.read_json(json.dumps(cells), orient="records")

        # fill missing outputs with empty list
        # we have to iterate through them, cannot do a bulk assignment
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

        pd.concat(frames).to_csv(args.notebook.replace("ipynb", "csv"))
