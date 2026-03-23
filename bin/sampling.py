import numpy as np
import pandas as pd


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


def collapse_clusters(
    data: pd.DataFrame, col: str, coverage_target: float = 0.7
) -> None:
    """Collapse existing clusters based on coverage_target."""
    cluster_sizes = data[col].value_counts()
    total = len(data)

    cumulative_coverage = cluster_sizes.cumsum() / total
    large_clusters = cumulative_coverage[
        cumulative_coverage <= coverage_target
    ].index.tolist()

    print(f"Large clusters  : {len(large_clusters)}")
    print(f"Coverage        : {cluster_sizes[large_clusters].sum() / total:.1%}")

    data[col] = data[col].apply(lambda c: c if c in large_clusters else -2)


def calculate_sample_size(total: int) -> int:
    """Standard formula: n = Z^2 · p(1-p) / e^2  (with finite-population correction)"""
    Z, p, e = 1.96, 0.5, 0.05
    n_inf = (Z**2 * p * (1 - p)) / e**2  # infinite population
    n_target = int(np.ceil(n_inf / (1 + (n_inf - 1) / total)))  # finite-pop correction
    return n_target


def main(data: pd.DataFrame, col: str):
    total = len(data)

    collapse_clusters(data, col)
    strata = data[col].value_counts()
    print(f"Total strata    : {len(strata)}")

    n_target = calculate_sample_size(total)
    print(f"Sample size    : {n_target}")

    sample = stratified_proportional_sampling(data, col, n_target)
    print(f"Sampled         : {len(sample)} items")

    return sample


if __name__ == "__main__":
    data = pd.read_csv("data/shome2023notebook/clusters-dedup.csv", index_col=0)

    GH = data.loc[data["CGH"].notna()]
    GH_sample = main(GH, "CGH")

    KG = data.loc[data["CKG"].notna()]
    KG_sample = main(KG, "CKG")

    print(f"GH sample: {GH_sample.shape} KG sample: {KG_sample.shape}")

    GH_sample.to_csv("data/shome2023notebook/GH_sample.csv", index=False)
    KG_sample.to_csv("data/shome2023notebook/KG_sample.csv", index=False)
