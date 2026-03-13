# Next Steps

I think that I am lacking basic understanding of how to arrive at a high-quality sample of notebooks.

The premise of the paper is mostly there. To avoid any red flags from reviewers, I think it's best to just follow the methodology of Wang 2025.
Additionally, consider reading a few more high-quality papers that use notebooks as their data.

I can easily get data collection done by end of March.
The paper can be written in April.

Back up the use of asserts, prints and last cell output (LCO).
Asserts are well strudied in SE research, prints and LCO are more trickly.
Our best bet, is to back this choice using literature.

Read relevant literature on ML bugs, faults, failures and crashes. Wang 2025 has a nice table that summarizes prior work. And we are already citing the taxonomy presented by Morovati 2024.

# Research Goal

The reseach goal is to *characterize* the validation methods used
in Jupyter notebooks to validate ML projects.

I think it's better to drop prints and simplify to validation methods.
Then we can clearly argue using existing work that:
- We look at the output of code cells since that is the predominant way data scientists validate their code
- And assertions form the backbone of automated software testing.
- By cross-cutting the analysis across implicit and explicit forms of validation, we can derive rich insights: e.g., the limitations of automated validation techniques for DS work. The implications can help design automated tests for ML.
- And then mapping it to existing taxonomy of NB bugs from Wang 2025.
Their taxonomy is rich, and encompases ML bugs.
We can find the overlaps and gaps of current validation techniques.

Still needs work, but I think the contributions are:
1. Large-scale dataset of *validation methods* used in Jupyter notebooks.
Mined from two distinct sources: GitHub and Kaggle.
A high level quantitative analysis of the data using descriptive and lexical analysis.
1. A qualitative analysis using case-study (or more appropriate) methodology to analyze X FMs and create a thematic mapping to existing work on ML bugs. Might need to strengthen the analysis here.
1. From this mapping we generate Y something.
1. A tight discussion section with implications for researchers and practitioners.

# Data Collection

I think that I lack a fundamental understanding of how to derive a high-quality sample of notebooks.
That's why I am reading a selection of high-quality papers from the past 3 years.
I am taking note of the research goal/questions of these papers,
and how they influenced their data collection,
and subsequent sampling methodology.
My objective is to find an appropriate data collection,
and sampling strategy, for this paper from this persuit.

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

# Research Methodology

Use [Baltes 2022](https://link-springer-com.tudelft.idm.oclc.org/article/10.1007/s10664-021-10072-8) for best practices on sampling.

I am unsure which qualitative methodology is appropriate for this paper.
In the current version, we claim to use case-study. Perhaps understand this methodology better?
I found the following papers:
- [Lenberg 2024](https://doi-org.tudelft.idm.oclc.org/10.1002/smr.2607): Qualitative software engineering research: Reflections and guidelines
- [Runeson 2008](https://link-springer-com.tudelft.idm.oclc.org/article/10.1007/S10664-008-9102-8): Guidelines for conducting and reporting case study research in software engineering. 

Perhaps also revisit the meta papers in my library.

# Relevant Literature

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
