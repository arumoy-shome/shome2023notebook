import pandas as pd

if __name__ == "__main__":
    data = pd.concat([
            pd.read_csv("data/shome2023notebook/GH_sample-annot.csv"),
            pd.read_csv("data/shome2023notebook/KG_sample-annot.csv")
        ], ignore_index=True)
    data = data.loc[data["EC"].isna()] # remove exclusions
    data["Type"] = data["Intent"].map(lambda x: x.split("-")[-1], na_action="ignore")
    data["Intent"] = data["Intent"].map(lambda x: x.split("-")[0], na_action="ignore")

    data.to_csv("data/shome2023notebook/annotations.csv", index=False)
