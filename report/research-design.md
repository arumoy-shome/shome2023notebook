# Next Steps
Back up the use of asserts, prints and last cell output (LCO).
Asserts are well strudied in SE research, prints and LCO are more trickly.
Our best bet, is to back this choice using literature.

Read relevant literature on ML bugs, faults, failures and crashes. Wang 2025 has a nice table that summarizes prior work. And we are already citing the taxonomy presented by Morovati 2024.

Read up on the case-study methodology.

# Data Collection
Reviewers raised concerns regarding the quality of the notebooks/projects mined from GitHub (but didn't care so much about the notebooks from Kaggle).

I read several papers that worked with notebooks, and none of them took quality measures (such as stars, forks, contributors, commits, etc.) into account.

It is too late to change the data sources and mine the data again. Stick with what we have, and instead strengthen the methodology section. Some ideas I have:
1. Discuss how we are deliberately making a trade-off between 2 threats to validity (not sure which ones though)
1. Cite prior papers that followed the same methodology.
1. Find or discuss how the sampling strategy & manual analysis addresses the quality concerns.
1. The mapping with existing work on bugs in ML validates our findings and speaks to the quality of the data.

# Research Methodology

I am unsure which qualitative methodology is appropriate for this paper.
In the current version, we claim to use case-study. Perhaps understand this methodology better?
I found the following papers:
- [Lenberg 2024](https://doi-org.tudelft.idm.oclc.org/10.1002/smr.2607): Qualitative software engineering research: Reflections and guidelines
- [Runeson 2008](https://link-springer-com.tudelft.idm.oclc.org/article/10.1007/S10664-008-9102-8): Guidelines for conducting and reporting case study research in software engineering. 

Perhaps also revisit the meta papers in my library.

# Relevant Literature

## [Wang 2025 (TSS)](https://dx.doi.org/10.1109/TSE.2025.3574500) 
The only paper to connect ML and notebooks.
They collected notebooks from GitHub and Kaggle, so we can use this.
Dataset available on [Zenodo](https://zenodo.org/records/15551901).

Highly relevant to this paper, use this for methodology and discussion.

Table 1 summarizes prior work on ML bugs, faults, failures and crashes.

They used *proportional stratified sampling* combined with *Jaccard similarity*. Could be something to consider in our paper as well.

## [Pimentel 2019 (MSR)](http://dx.doi.org/10.1109/MSR.2019.00077)
Code quality issues in notebooks.

## [Grotov 2020 (MSR)](http://dx.doi.org/10.1145/3524842.3528447)
Authors compared code quality in notebooks and scripts.
The data was collected from GitHub but the authors did not do any quality checks or filtering (e.g., stars, forks, contributors, etc.).
[Larsen 2025](https://dx.doi.org/10.1109/ESEM64174.2025.00030) published in ESEM 2025 and used Grotov's dataset.
So as long as, we use an already published dataset, we are okay.

## [Psallidas 2019 (ArXiv)](https://arxiv.org/abs/1912.09536)
Related or cited by papers could lead to something good.

## [Simmons 2020 (ESEM)](https://dl-acm-org.tudelft.idm.oclc.org/doi/pdf/10.1145/3382494.3410680)
This was published in ESEM and should be cited here.
The study design could be useful for some inspiration.

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
