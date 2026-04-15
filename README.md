# Understanding Feedback Mechanisms in Machine Learning Jupyter Notebooks

This repository contains the replication package for the research paper titled *Feedback Mechanisms in Machine Learning Jupyter Notebooks*.

In this project, I conducted a large scale empirical analysis of 3M Python code statements which I mined from 298K Jupyter notebooks (283GB) from Github and Kaggle.

Additionally, I conducted a qualitative analysis of 83 Python statements and proposed a taxonomy of feedback mechanisms used by Data Scientists when developing ML prototypes inside Jupyter notebooks. You can view the taxonomy here: <https://arumoy.me/shome2023notebook>

The dataset of Python code statements is shared under a CC license and [can be downloaded from this link](https://figshare.com/articles/dataset/Understanding_Feedback_Mechanisms_in_Jupyter_Notebooks/26372140). If you are interested, you can find the paper on [ArXiv](https://arxiv.org/abs/2408.00153).

## Scripts

The `bin/` directory contains the data collection and analysis pipeline. The scripts should be run in the following order:

### Running with Docker

The provided `Dockerfile` installs all Python dependencies from `requirements.txt`. Build the image once and then use it to run any script, mounting the repository as a volume so that inputs and outputs are read from and written to the local `data/` directory.

```bash
docker build -t shome2023notebook .
docker run --rm -v "$(pwd)":/app shome2023notebook bash bin/data-collection.bash
docker run --rm -v "$(pwd)":/app shome2023notebook bash bin/merge-datasets.bash
docker run --rm -v "$(pwd)":/app shome2023notebook python bin/clustering.py
docker run --rm -v "$(pwd)":/app shome2023notebook python bin/sampling.py
```

### 1. Data collection

`bin/data-collection.py` parses a single Jupyter notebook and extracts three types of Python statements into separate CSV files:

- **asserts**: `assert` statements and assertion function calls (e.g. `assertEqual`)
- **prints**: `print()` calls
- **lasts**: last statements of cells that produced an `execute_result` output

Only notebooks that import a ML library (`sklearn`, `torch`, `tensorflow`, or `keras`) are processed. Output CSVs are written to `data/shome2023notebook/` mirroring the input path.

`bin/data-collection.bash` runs `data-collection.py` in parallel (8 workers) over all notebooks in `data/`.

```bash
bash bin/data-collection.bash
```

### 2. Merging datasets

`bin/merge-datasets.bash` concatenates the per-notebook `*-{stats,prints,asserts,lasts}.csv`, files produced by the data collection step into a single CSV file.

```bash
bash bin/merge-datasets.bash
```

### 3. Clustering

`bin/clustering.py` embeds the collected statements using [CodeBERT](https://huggingface.co/microsoft/codebert-base) (CLS-token, float16), reduces dimensionality with UMAP, and clusters with HDBSCAN. Three sets of cluster labels are produced: one over all statements (`CALL`), one over GitHub statements only (`CGH`), and one over Kaggle statements only (`CKG`). Results are written to `data/shome2023notebook/clusters.csv`.

```bash
python bin/clustering.py
```

### 4. Sampling

`bin/sampling.py` reads `data/shome2023notebook/clusters.csv` (the cluster output) and draws a stratified proportional sample from each source (GitHub and Kaggle) using the standard finite-population correction formula (95% confidence, 5% margin of error). Samples are written to `data/shome2023notebook/GH_sample.csv` and `data/shome2023notebook/KG_sample.csv`.

```bash
python bin/sampling.py
```

Modify and use `bin/resampling.py` to resample interactively from specific population (GH or KG) and cluster as required.

### 5. Merge annotations

The open-coding is done using Google Sheets. Use `merge-annotations.py` to merge the annotated csv files into a single `data/shome2023notebook/annotations.csv` file.

## Notebooks

The data analysis is conducted using Jupyter notebooks located in the `notebooks/` directory.

### 1. Raw numbers and statistics

`notebooks/data-collection-numbers.ipynb` contains raw numbers and statistics
from the data collection process.

### 2. Results analysis

`notebooks/results.ipynb` contains all analysis of the annotated data.

## Building PDF files

All latex source files are located inside the `report/` directory. You can use the `latexmk` command (included in the full distribution of LaTeX) to build the PDF document.

```
cd report/
latexmk -pdf --synctex=1 -f emse24.tex
```

Alternatively, if you don't want to install the entire tex distribution, you can use the `tectonic` <https://tectonic-typesetting.github.io/en-US/> command to build the PDF.

```
tectonic --synctex report/emse24.tex
```

## Generating diff documents

Use the `latexdiff` command to create a tex file that shows the difference between two latex files.

``` bash
latexdiff old.tex new.tex >diff.tex
```

## Document changelog

### EMSE
1. report/emse24.tex: original EMSE submission
2. report/emse24-revised.tex: revised version (resubmitted to EMSE)
3. report/emse24-response.tex: response document for the first round of reviews
4. report/emse24-diff.tex: diff between emse24.tex and emse24-revised.tex

### ESEM
1. report/main.tex: ESEM submission (LIPIcs format)

### Other conference papers
- report/icse24-nlbse.tex: ICSE 2024 NLBSE workshop paper
- report/icst24.tex: ICST 2024 paper

## Data
1. `asserts.csv`, `prints.csv`, `lasts.csv` and `stats.csv` contain the raw data collected.
1. `clusters.csv` and `clusters-dedup.csv` contain asserts and last statements with clustering annotation.
1. `GH_sample.csv` and `KG_sample.csv` contain a representative sample from each source using proportional stratified sampling.
1. `GH_sample-annot.csv` and `KG_sample-annot.csv` contain the open coding annotations.
