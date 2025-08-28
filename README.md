# Understanding Feedback Machanisms in Machine Learning Jupyter Notebooks

This repository contains the replication package for the research paper titled *Feedback Mechanisms in Machine Learning Jupyter Notebooks*. 

In this project, I conducted a large scale empirical analysis of 3M Python code statements which I mined from 298K Jupyter notebooks (283GB) from Github and Kaggle.

Additionally, I conducted a qualitative analysis of 83 Python statements and proposed a taxonomy of feedback mechanisms used by Data Scientists when developing ML prototypes inside Jupyter notebooks. You can view the taxonomy here: <https://arumoy.me/shome2023notebook>

The dataset of Python code statements is shared under a CC license and [can be downloaded from this link](https://figshare.com/articles/dataset/Understanding_Feedback_Mechanisms_in_Jupyter_Notebooks/26372140). If you are interested, you can find the paper on [ArXiv](https://arxiv.org/abs/2408.00153).

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

## EMSE document changelog
1. report/emse24.tex: this is the original EMSE submission
2. report/emse24-revised.tex: this is the revised version (resubmitted to EMSE)
3. report/emse24-response.tex: this is the response document for the first round of reviews (received on emse24.tex)
4. report/emse24-diff.tex: diff between emse24.tex and emse24-revised.tex
