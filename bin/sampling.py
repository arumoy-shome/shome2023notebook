import numpy as np
import pandas as pd
import seaborn as sns


def stratified_proportional_sampling(
    data: pd.DataFrame, col: str, size: int = 384
) -> pd.DataFrame:
    counts = data[col].value_counts()
    exact = counts * size / len(data)
    floored = np.floor(exact).astype(int)
    floored = floored.clip(lower=1)

    # Distribute remaining slots by largest remainder
    remainder = size - floored.sum()
    remainders = (exact - floored).nlargest(remainder).index
    floored[remainders] += 1

    # Sample each group
    frames = [
        group.sample(n=floored[name], random_state=42)
        for name, group in data.groupby(col)
    ]
    return pd.concat(frames).reset_index(drop=True)


if __name__ == "__main__":
    data = pd.read_csv("data/shome2023notebook/clusters-dedup.csv", index_col=0)

    GH = data.loc[data["CGH"].notna()]
    KG = data.loc[data["CKG"].notna()]

    GH_sample = stratified_proportional_sampling(data=GH, col="CGH")
    KG_sample = stratified_proportional_sampling(data=KG, col="CKG")

    print(f"GH sample: {GH_sample.shape} KG sample: {KG_sample.shape}")

    GH_sample.to_csv("data/shome2023notebook/GH_sample.csv", index=False)
    KG_sample.to_csv("data/shome2023notebook/KG_sample.csv", index=False)
