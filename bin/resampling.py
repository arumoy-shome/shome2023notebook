# %%
import pandas as pd
from bin.sampling import collapse_clusters

# %%
data = pd.read_csv("data/shome2023notebook/clusters-dedup.csv", index_col=0)
GH = data.loc[data["source"] == "GH"]
KG = data.loc[data["source"] == "KG"]

# %%
collapse_clusters(GH, "CGH")
collapse_clusters(KG, "CKG")

# %%
sample = KG.loc[KG["CKG"] == 623].sample(1)

# %%
