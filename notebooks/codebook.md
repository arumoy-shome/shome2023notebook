---
title: "Codebook"
format: pdf
---

We used open-coding to manually analyze a representative sample of validation methods from both GH and KG.

The analysis considered two dimensions:
- Dimension A: Identifying the functional intent of the statement.
- Dimension B: The machine learning development lifecycle stage in which the statement was defined.

## Dimension A Codebook 
| Code | Label | Definition | Example |
| ------------- | -------------- | :------------: | ------------- |
| VAL-EQ | Value equality check | Assert that a result equals a known correct value. Also use when `in` operator with a literal collection in RHS is used. | `assert dataY[0] == 35`, `assert type in ['healthy', 'failed']`, `assert_frame_equal(...)`, `np.testing.assert_array_equal(...)` |
| VAL-EXIST | Check for existance of value | Assert that checks if a value exists inside a dynamically generated collection in RHS. | `assert i in sig.parameters.keys()` |
| VAL-SHAPE | Dimensionality check | Assert tensor/array shape or length. Includes inequality checks on shape attributes. | `assert x.shape == means.shape`, `assert x.ndim > 1`, `assert len(x) >= 10` |
| VAL-TYPE | Type check | Assert object type or class membership. | `assert type(embedding_layer) == Embedding` |
| VAL-APPROX | Approximate equality | Assert numerical closeness within tolerance. Include manually expressed tolerance checks. | `assert np.allclose(..., atol=0.001)`, `np.isclose`, `np.abs(...) < 0.001` |
| VAL-BOOL | Boolean invariant | Assert a boolean condition holds. | `assert bb2['y1'] < bb2[y2]` |
| EXP-INSPECT | Object inspection | Display an object as-is (no transformation applied) to visually verify its contents. Include visualizations whose primary purpose is to _display_ the state of the data object or model output. | `decoder_prediction`, `sr_items`, `plt.imshow`, `sns.heatmap(...)`, `.head()` |
| EXP-STATS | Statistical summary | Compute and display descriptive statistics. Include visualizations that provide statistical summaries. | `kindel_reviews.summary_length.describe(...)`, `plt.hist(...)`, `df.describe()` |
| EXP-STRUCT | Structural probe | Inspect shape, size, keys, columns, type metadata. | `wv.vector_size`, `dir(tf.math)`, `df.shape`, `df.columns`, `df.dtypes`, `len(x)`, `.unique()` (cardinality) |
| EXP-COMPUTE | Exploratory computation | Apply a function or transformation and inspect the result. | `softmax(np.array([[1, 2, 3]]) - 1)`, `.sort_values()` |

The top level splits are:

- VAL: verification, programmer knows expected value
- EXP: exploration, programmer is discovering

## Dimension B Codebook

| Code   | Stage                         | Signals to look for                                     |
| ------ | ----------------------------- | ------------------------------------------------------- |
| DATA   | Data loading/ingestion        | `read_csv`, `load`, file paths, dataset names           |
| PREP   | Preprocessing/cleaning        | `transform`, `normalize`, `fillna`, `encode`, tokenize  |
| FEAT   | Feature engineering           | `fit`, `vectorize`, embeddings, `TF-IDF`                |
| MODEL  | Model definition              | `model = ...`, layer definitions, `output_shape`        |
| TRAIN  | Training/optimization         | `model.fit`, `epochs`, loss, `grid.fit`                 |
| EVAL   | Evaluation/metrics            | `predict`, `score`, `pearsonr`, `mse`, confusion matrix |
| UNC    | Unclear                       | Insufficient context from statement alone               |

## Exclusion Criteria
| Code | Definition |
| ---- | ---------- |
| HW | Assert statements written in academic notebooks with assignments (e.g., autograder). |
| ERR | Misuse of notebook cells e.g., writing documentation using block quotes in a code cell (rather than using a markdown cell), or code that was commented out but not reexecuted (so still had stale output). |
| ENG | Statement and/or notebook not authored in English. |
| NOINT | No functionl intent relevant to this study e.g., `plt.ylabel('Win %')`. |
| NOML | Statements that perform scientific simulations/computations, but do not train any ML model. These statements were captured since the notebooks import statistical computation functions implemented in the library we used to identify ML related notebooks. |
| EXP | Statements used to quickly explore an API or how an imported function works. |
