# Research Goal

The reseach goal is to *characterize* the validation methods used
in ML Jupyter notebooks.

Then we can clearly argue using existing work that:
- We look at the output of code cells since that is the predominant way data scientists validate their code (back with Rule, Head and Kery).
- And assertions form the backbone of automated software testing.
- By cross-cutting the analysis across implicit and explicit forms of validation, we can derive rich insights: e.g., the limitations of automated validation techniques for DS work. The implications can help design automated tests for ML.
- And then mapping it to existing taxonomy of NB bugs from Wang 2025.
Their taxonomy is rich, and encompases ML bugs.
We can find the overlaps and gaps of current validation techniques.

## Contributions

1. Large-scale dataset of *validation methods* used in Jupyter notebooks.
Mined from two distinct sources: GitHub and Kaggle.
A high level quantitative analysis of the data using descriptive and lexical analysis.
1. A qualitative analysis using case-study (or more appropriate) methodology to analyze X FMs and create a thematic mapping to existing work on ML bugs. Might need to strengthen the analysis here.
1. From this mapping we generate Y something.
1. A tight discussion section with implications for researchers and practitioners.

# Data Analysis

We used open-coding to manually analyze a representative sample of validation methods from both GH and KG.

The analysis considered two dimensions:
- Dimension A: Identifying the functional intent of the statement.
- Dimension B: The machine learning development lifecycle stage in which the statement was defined.

## Dimension A Codebook 
| Code | Label | Definition | Example |
| ------------- | -------------- | :------------: | ------------- |
| VAL-EQ | Value equality check | Assert that a result equals a known correct value. Also use when `in` operator with a literal collection in RHS is used. | `assert dataY[0] == 35` or `assert type in ['healthy', 'failed']` |
| VAL-EXIST | Check for existance of value | Assert that checks if a value exists inside a dynamically generated collection in RHS. | `assert i in sig.parameters.keys()` |
| VAL-SHAPE | Dimensionality check | Assert tensor/array shape or length. | `assert x.shape == means.shape` |
| VAL-TYPE | Type check | Assert object type or class membership. | `assert type(embedding_layer) == Embedding` |
| VAL-APPROX | Approximate equality | Assert numerical closeness within tolerance. | `assert np.allclose(..., atol=0.001)` |
| VAL-BOOL | Boolean invariant | Assert a boolean condition holds. | `assert bb2['y1'] < bb2[y2]` |
| EXP-INSPECT | Object inspection | Display an object as-is (no transformation applied) to visually verify its contents. | `decoder_prediction`, `sr_items` |
| EXP-STATS | Statistical summary | Compute and display descriptive statistics. | `kindel_reviews.summary_length.describe(...)`, `plt.hist(...)`, `df.describe()` |
| EXP-STRUCT | Structural probe | Inspect shape, size, keys, columns, type metadata. | `wv.vector_size`, `dir(tf.math)`, `df.shape`, `df.columns`, `df.dtypes`, `len(x)`, `.unique()` (cardinality) |
| EXP-COMPUTE | Exploratory computation | Apply a function or transformation and inspect the result. | `softmax(np.array([[1, 2, 3]]) - 1)` |
| DOC | Documentation display | Output primarily for communicating to a notebook reader. | f-string narrating what happened |

The top level splits are:

- VAL: verification, programmer knows expected value
- EXP: exploration, programmer is discovering
- DOC: communication to reader

## Dimension B Codebook

| Code   | Stage                         | Signals to look for                                     |
| ------ | ----------------------------- | ------------------------------------------------------- |
| DATA   | Data loading/ingestion        | `read_csv`, `load`, file paths, dataset names           |
| PREP   | Preprocessing/cleaning        | `transform`, `normalize`, `fillna`, `encode`, tokenize  |
| FEAT   | Feature engineering           | `fit`, `vectorize`, embeddings, `TF-IDF`                |
| MODEL  | Model definition              | `model = ...`, layer definitions, `output_shape`        |
| TRAIN  | Training/optimization         | `model.fit`, `epochs`, loss, `grid.fit`                 |
| EVAL   | Evaluation/metrics            | `predict`, `score`, `pearsonr`, `mse`, confusion matrix |
| INTERP | Interpretation/explainability | `interpret`, `feature_importance`, SHAP, attention      |
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
# Relevant Literature

## [Chan 1996](https://doi-org.tudelft.idm.oclc.org/10.1016/0950-5849(96)01103-2)

Wang 2025 uses this paper to justify sampling at least 1 example from each cluster.
We should do the same.

## [Jiang 2025 (ESEM)](https://dx.doi.org/10.1109/ESEM64174.2025.00052)
**Exploring the Jupyter Ecosystem: An Empirical Study of Bugs and Vulnerabilities**

Most recent paper published in ESEM on Jupyter notebooks.

Notebooks (NB) collected both from GitHub (GH) and Kaggle (KG).
1000 NBs from GB, sorted by star rating.
Filtered out inactive projects (automatic; based on GH activities)
and non-dev projects (manual; README).

In particular,
they first used clustering to identify groups based on code similarity,
then randomly sampled 30--50 instances from each group.
The instances were analyzed independently by 3 authors, in 3 iterations.
The search was stopped when no authors found any new insights.

## [Wang 2025 (TSS)](https://dx.doi.org/10.1109/TSE.2025.3574500) 
The only paper to connect ML and notebooks.
They collected notebooks from GitHub and Kaggle, so we can use this.
Dataset available on [Zenodo](https://zenodo.org/records/15551901).

Highly relevant to this paper, use this for methodology and discussion.

Table 1 summarizes prior work on ML bugs, faults, failures and crashes.

Proportional stratified sampling was used to identify instances.
This sampling technique divides the propulation into strata
and randomly samples from within, in proportion to their size.
They used Jaccard similarity to define the strata.

## [Ghahfarokhi 2024 (MSR)](https://doi-org.tudelft.idm.oclc.org/10.1145/3643991.364488)
DistilKaggle dataset.

## [De Santana 2024 (TOSEM)](https://doi-org.tudelft.idm.oclc.org/10.1145/3641539) 

## [Patra 2022 (ICSE)](https://doi-org.tudelft.idm.oclc.org/10.1145/3510003.3510144) 
Nalin: Name-value inconsistencies in Jupyter notebooks

## [Grotov 2022 (MSR)](http://dx.doi.org/10.1145/3524842.3528447)
Authors compared code quality in notebooks and scripts.
The data was collected from GitHub but the authors did not do any quality checks or filtering (e.g., stars, forks, contributors, etc.).
[Larsen 2025](https://dx.doi.org/10.1109/ESEM64174.2025.00030) published in ESEM 2025 and used Grotov's dataset.
So as long as, we use an already published dataset, we are okay.

## [Pimentel 2019 (MSR)](http://dx.doi.org/10.1109/MSR.2019.00077)
Code quality issues in notebooks.

## [Psallidas 2019 (ArXiv)](https://arxiv.org/abs/1912.09536)
Related or cited by papers could lead to something good.

## [Simmons 2020 (ESEM)](https://dl-acm-org.tudelft.idm.oclc.org/doi/pdf/10.1145/3382494.3410680)
This was published in ESEM and should be cited here.
Could be useful for the narrative.

## [Nahar 2025 (ICSE)](https://dx.doi.org/10.1109/ICSE55347.2025.00006)
Nahar proposed a high-quality dataset of open source ML products.
[Supplemental material](https://osf.io/gqyex/overview) contains list of all projects.
I randomly looked at 5 projects from this list, non of them had a notebook in the main branch.
Could expand search to entire git history?

This paper also used a combination of quantitative and qualitative research methods. Use this paper to guide our writing.

## [Jiang 2022 (ICSME)](https://dx.doi.org/10.1109/ICSME55016.2022.00047)
This paper was published in ICSME 2022.
The research objective of the paper is to support tool development for notebooks
to facilitate code understanding, modularization, and maintenance.

The proposed algorithm labels the notebook cells
as per the stages of the ML development lifecycle (e.g., data collection, model training).

Used "def-use" chains for data flow analysis.
In this context, data flow does not refer to the dataset,
but to the flow of information through the functions.

What's interesting to me is the data collection strategy.
Authors downloaded **all** notebooks published on 2 separate dates,
which represent the random sample of notebooks.

## [Siddik 2025 (JSS)](https://doi-org.tudelft.idm.oclc.org/10.1016/j.jss.2025.112758)
SLR of SE research on Jupyter notebooks.
The paper presents a good overview of research efforts on Jupyter notebooks.
I didn't find anything that links with the narrative of this paper,
although keeping this paper handy for future reference.

The paper identified 11 themes of research:
- Code reuse & provenance
- Managing computational environment & workflow
- Readability of NBs
- Documentation of NBs
- Testing & debugging
- Visualization in NBs
- Best practices
- Cell execution order
- NB code generation
- Support for other programming paradigms

Of which, "Testing & debugging" and "Visualizations in NBs" can be of particular interest.
