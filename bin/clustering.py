import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.cluster import HDBSCAN
from sklearn.pipeline import Pipeline
import umap
from tqdm import tqdm

def embed_batch(texts: list[str], batch_size: int = 32) -> np.ndarray:
    """Return CLS-token embeddings, shape (n, 768)."""
    all_vecs = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Embedding"):
        batch = texts[i : i + batch_size]
        enc = tokenizer (
            batch,
            padding=True,
            truncation=True,
            max_length=128, # assert statements are short
            return_tensors="pt",
        ).to(device)
        with torch.no_grad():
            out = model(**enc)
        # CLS token = out.last_hidden_state[:, 0, :]
        vecs = out.last_hidden_state[:, 0, :].cpu().numpy()
        all_vecs.append(vecs)
    return np.vstack(all_vecs)

if __name__ == "__main__":
    asserts = pd.read_csv(
        "data/shome2023notebook/asserts.csv",
        header=None,
        names=["notebook", "stmt"]
    )
    lasts = pd.read_csv(
        "data/shome2023notebook/lasts.csv",
        header=None,
        names=["notebook", "stmt"]
    )
    data = pd.concat([asserts, lasts], ignore_index=True)
    data.loc[data["notebook"].str.contains(r"^data/assert"), "source"] = "GH"
    data.loc[data["notebook"].str.contains(r"^data/quaranta"), "source"] = "KG"
    data = data.sample(frac=0.001)
    data = data.dropna()
    print(f"data sample size: {data.shape}")

    MODEL = "microsoft/codebert-base"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModel.from_pretrained(MODEL)
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    pipeline = Pipeline([
        ("reducer", umap.UMAP(
            n_components=10,
            n_neighbors=15,
            min_dist=0.0,
            metric="cosine",
            random_state=42,
        )),
        ("clusterer", HDBSCAN(
            min_cluster_size=50,
            min_samples=5,
            metric="euclidean",
            cluster_selection_method="eom",
        )),
    ])

    # NOTE: embed once, then use mask to obtain XGH and XKG
    X = embed_batch(data["stmt"].to_list())  # (n_samples, 768)

    gh_mask = (data["source"] == "GH").values
    kg_mask = (data["source"] == "KG").values

    XGH = X[gh_mask]
    XKG = X[kg_mask]

    # NOTE: add the cluster labels back to data
    data.loc[:, "CALL"] = pipeline.fit_predict(X)
    data.loc[data["source"] == "GH", "CGH"] = pipeline.fit_predict(XGH)
    data.loc[data["source"] == "KG", "CKG"] = pipeline.fit_predict(XKG)

    data.to_csv("data/shome2023notebook/clusters.csv")
