
# @method open card sorting

I learned about the open-card sorting from kochhar2017. It's basically what I did for the EMSE paper, only I didn't know it had a format definition before.

# @idea do asserts fail and why?

Collect the `stderr` outputs of jupyter cells and analyse them?

# experiments with outputs of notebooks

+ a cell can have multiple outputs if they are of different types, for example: a `print` and last statement can co-exist since they are of different output types
+ any number of visualisation statements appearing prior to the last statement can co-exist
   + however, the inverse is not true ie. if there are multiple `df.head()` statements prior to a visualisation statement, only the visualisation output is kept (I suspect because they are both of the same output type?)

The bottom line is that we need to isolate cells that only have a single output

# role of feedback and agile development

Following recommendations from Diomidis regarding the role of feedback in agile development:

+ https://pubs.opengroup.org/opengrouppress/managing-digital/systems-thinking.html
+ https://pubs.opengroup.org/opengrouppress/managing-digital/chapter-app-deliv.html (figure 43)

# big numbers from the analysis

+ number of code cells with keyword "assert" (github): 44751
+ number of code cells with keyword "assert" (kaggle): 5897

+ number of code cells with output (github): 357661
+ number of code cells with output (kaggle): 1945425

# 2024-03-29 story for ESEM '24 paper (revised)

We had another meeting with Diomidis and Luis and the discussion there helped finalise the story much more. Here it goes:

We begin with a high-level overview of the ML lifecycle--here we highlight how there are several components that we need to think about when developing ML pipelines. ML pipelines are seldom developed in isolation, inside source code files. Instead, they require a more interactive and iterative approach.

Computational Notebooks have been widely adopted for developing ML pipelines which they support such an iterative development process. Within the Python ML community, Jupyter has been widely popular (this is why we mine Jupyter Notebooks in particular).

However, traditional practices of writing test suites to ensure the correctness of ML pipelines fail to adapt to this new paradigm of development. Often, checks are performed manually by the developer by simply observing the output of a code cell. Alternatively, assert statements are far more suited for testing within computational notebooks (**TODO** this requires a bit more thought and fine-tuning; how we want to integrate the implicit vs explicit testing).

RQ1: How are the outputs of code cells used for testing ML pipelines?

    Here we have present the descriptive and lexical analysis of the outputs of code cells.

    RQ1.1: We have to distinguish here between explicit outputs produced with `print` statements and
    RQ1.2: Implicit outputs from the last statement of a code cell.

RQ2: How are assertions used for testing ML pipelines?

    Here we present the descriptive and lexical analysis of code cells with assertions.

    RQ2.1: Compare and contrast between outputs vs assertions. What are the similarities? Differences?

RQ3: How are visualisations used to test ML pipelines?

    Decisions are not only made using text output in ML pipelines; we use visualisations to understand complexity of the dataset and ML models. Visualisations are a special form of manual test using outputs.

    Extend the descriptive and lexical analysis performed earlier, to code cells that produce a visualisation.

    RQ3.1: Are assertions written to test visual insights gained from visualisations?

    Here we dump all the content from the ICST paper.

# 2024-03-22 story for ESEM '24 paper

Since visualisations are no longer the headline for this paper, I need
to revisit the story/motivation of what we are trying to do.

The kochhar2017revisiting provided some foundation for this. We need to
start with background of assertions as an alternative means of testing
(compared to more traditional test suites written in dedicated test
files).

Then we need to justify why assertions are a good fit for testing ML
projects. We can ellaborate how developing ML software is highly
iterative and requires a lot of experimentation.

Then bring in the popularity of computational notebooks since they
support this iterative style of development. This is also our reasoning
for collecting assertions from Jupyter notebooks.

Then we bring in the large-scale empirical analysis of assert statements
in notebooks that we are performing. Here we highlight the descriptive
statistics and analysis we conducted.

Next, we go into analysing the outputs of code cells as a means of
manually validating pre/post conditions or expectations of
developers. We start by analysing the "text/plain" outputs of
cells. Next we present the use of visualisations as a more specialised
case of this manual validation. Here, we want to highlight these cases
of missed opportunities where assertions can be used to make the
expectations of developers explicit.

# 2024-03-07 brainstorming with Diomidis

Diomidis gave a strong impression that the empirical study of `assert` statements in Python Jupyter Notebooks is a promising direction.

He had the following suggestions for RQs of the paper:
1. "Density" of `assert` statements: this entails the general statistics we are collecting such as:
   + number of code cells in the NB
   + number of markdown cells in the NB
   + number of code cells with at least 1 `assert` statement
2. Presence of a message when an `assert` fails
3. Lexical content: we are collecting the entire contents of the code cells with an `assert` statement
4. Lexical context: we are also collecting the entire contents of cells (code or markdown) above and below `assert` statements
5. We are also contributing the dataset of Python assert statements.

For the following re-submission, we are primarily focusing on assertions. But the the dataset we are creating, we will also be able to look into how assertions and visualisations interact with one-another.

Diomidis also proposed that we can create a taxonomy of assert statements. We take a meaningful sample, and create a taxonomy on that. Luis needs to do this as well so that we can calculate the Inter-Rater Agreement.

# Better documemtation for python `ast` module

[Green Tree Snakes](https://greentreesnakes.readthedocs.io/en/latest/)
is an external project that has better documentation for working with
the Python `ast` module. Link obtained directly from Python
documentation page for the `ast` module.

# 2024-02-28 luis-aru weekly next steps for ICST resubmission

We agreed that the human study is beneficial for the phd (it probably Will appear as the first chapter of the thesis); but for now we need to beef up the ICST '24 paper with more analytical analysis of `assert` statements and close this chapter.

I have changed my focus for the coming weeks to analysing the Kaggle dataset and performing the analysis.

## Ideas for `assert` analytics

Following some ideas for collecting analytics from Jupyter notebooks regarding assertions in them:

1. Starting from the notebook level:
   + How many notebooks with/without asserts in the original source?
2. Then at the cell level:
   + Ratio of code cells with asserts vs. without asserts? 
   + Relative position of code cells with assertions (within the notebook)? This one is inspired by quaranta2021kgtorrent.
   + Contents/keywords of code cell with assert? Similarly, contents/keywords of code cell above the assert? The goal here is to understand/analyse the keywords typically present within assertions. With the analysis of the code cells above the assert is to study if there are patterns in the code that lead to an assertion.

# 2024-02-25 SBERT for automatically identifying related VA pairs

I had a chat with Jonathan last week. He originally mentioned SBERT
for the translation task. Although we cannot use it for that, I think
it fits the bill for automatically identifying related VA pairs.

# 2024-02-13 downloading from Zenodo

Zenodo API urls for datsets we are interested in:
1. mondal2023cell2doc:
    + base: <https://zenodo.org/api/records/10655071>
    + file: <https://zenodo.org/api/records/10655071/files/Cell2Doc-Artifacts.zip/content>
2. quaranta2021kgtorrent:
    + base: <https://zenodo.org/api/records/4468523>
    + file: <https://zenodo.org/api/records/4468523/files/KT_dataset.tar.bz2/content>

Get the download url using `curl` on the main records url (note down
the md5 checksum hash for later):

```sh
# replace with correct records id
curl --cookie zenodo.txt 'https://zenodo.org/api/records/xxxxxx?token=<>'
```

Then download:

```sh
curl --cookie zenodo.txt 'https://zenodo.org/api/records/8265137/files/Cell2Doc-Artifacts.zip/content?token=<>' --output Cell2Doc-Artifacts.zip
```

Where `token` is the Zenodo API key.

Validate that data is complete:

```sh
md5 Cell2Doc-Artifacts.zip
```

# 2024-02-12 review and planning

There are 3 tracks that I need to work on moving forward:
1. **Data Annotations**: Luis is already helping annotate the original VA
   pairs from Github. I might need to jump into annotations for VA
   pairs collected from Kaggle is the preliminary study returns
   positive results.
2. **Data Collection**: The existing VA pairs from Github are bogus. And
   we need a high quality dataset if we want to fine-tune LLMs since
   current code LLMs do not understand the kind of code-translation we
   are trying to do. Before moving on to KGTorrent dataset which is
   massive, I am trying to replicate my existing scripts on the
   mondal2023cell2doc dataset which is only 5K notebooks extracted
   from KGTorrent.
3. **LLM fine-tuning**: Assume that we fix the data-quality issue,
   I still have a lot to do with setting up the pipeline for
   fine-tuning or prompting the LLMs. Each model is unique, and this
   will also take considerable amount of time.

The biggest threat we currently have is that our VA pairs turn out to
be not good enough to produce meaningful results in existing LLMs. We
have 2 strategies for moving forward when this happens:

1. Pivot the ASE papers's focus to the presence of `assert` statements
   in Jupyter notebooks. We conduct more general analytics with the
   entire corpus of notebooks to strengthen our position on the
   importance of assertions and how this is not being done yet.
2. Propose an entirely new LLM capable of translating visualisation
   code to assertions.

# 2024-01-24 Meeting with Mali

## Models (focus on code input)
+ CodeBERT (start here)
+ Incoder (Meta)
+ CodeT5+
+ UnixCoder
+ ChatGPT 3.5 turbo

## Evaluation strategy
+ Cross-validation
+ No data leakage

# Bsc. Research Project Proposal

Based on dicussion during the group meeting and Luis, the proposal
should highlight our vision for whats to come after the ASE 2024
paper.

Our propsal should focus on the integration of the tool proposed in
the ASE '24 into existing software development workflows. One approach
here, would be to propose an itegration with VSCode, similar to the
Github Co-pilot integration.

The research questions can then be divided into exploring different
multi-modal data sources for the tool and perform an empirical study.

Another suggestion from Luis, was to investigate code-smells
specifically in visualisation code. We can check the feasibility of
this idea and decide is worth integrating this functionality into our
existing tool.

# ASE 2024 Paper Overview

Following is the execution plan for the ASE '24 paper which is due
first week of June.

1. We start from the data sources: Github. Here we have already mined
   1.7K notebooks with the `assert` statement. I have also manually
   assessed these notebooks and identified 269 VA-pairs which are
   semantically related to one-another. Our next plan is to
   re-annotate a sample size of 15% with Luis and calculate the
   inter-rater agreement.
2. Step 2 is to create the taxonomy of ML verification tasks using
   visualisations using the 269 VA-pairs. Here, I think again we need
   multiple annotators and calculate the agreement rate.
3. Next, using the taxonomy, we identify 1-2 validation tasks that we
   want to focus on. This forms the training and testing set for the
   LLM models. We want to run an empirical analysis to identify the
   best model which forms the base for our automated tool.
4. While running the empirical analysis, we also run the training data
   through ChatGPT and collect the responses. We compare and contrast
   the responses from ChatGPT to that of our tool.
5. Final step of the study, is to run a user study. The users will use
   our tool and report their experience followed by some post-study
   questions. We still need to finalise the contents of the study, but
   we have 2 ideas here:
    + first, most simple approach would be to recruite participants
      from within the research group.
    + second, if the timelines works out, we can use students from
      Luis's course to run the study.

## Additional comments/suggestions

1. We can extend the dataset and taxonomy using notebooks collected
   from Kaggle. There is literature to suggest that the data quality
   from Kaggle is superior to that of Github.
2. Mali's suggestion was to extract the taxonomy into a separate
   paper. If we are able to create the Kaggle dataset, then we can
   integrate this into this taxonomy paper as well.

# Automatically identifying related VA-pairs

We can use code similarity metrics for automatically flagging
notebooks that contain related VA-pairs.

When we do this manually, we mainly look at the parameters passed to
say `assert(...)` and `plt.plot(...)`.

I think this can be presented as a tool paper, and should be doable in
2-3 month sprint.

The tasks include:
+ feature engineering to figure out the best input set
+ experimenting with various code similarity metrics
+ determining the right number of samples (using power law) for statistically significant results

# Extending VA-pairs dataset with Kaggle Notebooks

We are thinking of presenting this extension as a MSR paper, rather
than including it in this study.

# Response from ChatGPT on how to generate prompts for this study
For each phase of the experimental design, creating effective prompts
is crucial for generating meaningful and accurate assertions. Here are
some recommended prompts for each phase:

### Phase 1: Assertions Based on Visualizations

1. **Descriptive Prompt:**
   - "Here is a visualization of a machine learning model's
     performance. Please observe the trends, patterns, and key
     features in the graph and generate assert statements that
     validate these observations."

2. **Guided Inquiry:**
   - "Examine this ML model accuracy chart. Identify any unusual
     peaks, drops, or inconsistencies in the data, and write assert
     statements that would flag such anomalies in future data."

3. **Comparative Analysis:**
   - "Given this comparative visualization of two different ML models,
     generate assert statements that could be used to ensure one model
     consistently outperforms the other under similar conditions."

### Phase 2: Assertions Based on Visualization Code

1. **Code Analysis:**
   - "Here is the Python code used to generate a visualization of an
     ML model's error rates. Analyze the code, especially the data
     processing and plotting parts, and write assert statements that
     would validate the correctness of future visualizations generated
     by similar code."

2. **Parameter Focus:**
   - "This code snippet creates a confusion matrix for
     a classification model. Please generate assert statements that
     ensure the matrix dimensions and values remain within expected
     ranges, considering the model's number of classes and sample
     sizes."

3. **Code Intent Understanding:**
   - "Review the following Python script intended to plot a ROC curve
     for a binary classifier. Generate assert statements that ensure
     the plot accurately reflects the model's true positive and false
     positive rates across various thresholds."

### Phase 3: Assertions Using Both Visualizations and Code

1. **Integrated Analysis:**
   - "Given both the visualization of an ML model's training history
     and the corresponding Python code, generate assert statements
     that ensure the training process, as depicted in the
     visualization, adheres to expected patterns in terms of loss
     reduction and accuracy improvement."

2. **Correlation Emphasis:**
   - "Here is the code for generating a feature importance plot and
     the plot itself. Develop assert statements that would verify the
     consistency and correctness of feature rankings as shown in the
     plot, based on the code's methodology."

3. **Comprehensive Validation:**
   - "Examine this scatter plot of predictions vs. actual values and
     its generating code. Write assert statements that validate both
     the integrity of the data processing in the code and the accuracy
     of the depicted predictions."

By tailoring the prompts to focus on specific aspects of the
visualizations and code, you can guide ChatGPT to generate more
relevant and precise assert statements, enhancing the quality of the
results for your study.

# Week of Oct 30 - Nov 05 Our next objective is to automate creating
the assertion given an ML/AI visualisation. I am experimenting with
ChatGPT 4.0 since it is the only LLM (right now) which supports image
input.

I passed the cherry-picked VA pairs from the ICST24 paper and passed
it through ChatGPT. I tried 3 prompting techniques, along with the
observations below:
1. Image only: okay-ish results, model hallucinates because it does
not have enough context; some results were spot-on
2. Visualisation code only: sometimes better than image only; other
times the assertions were really off
3. Image & Code: For the SVM-Acc pair, the assertion was spot-on.

The results from the above experiment are inconclusive at best. Given
the current trends and that I am doing SE research, I want to
double-down on prompting with code.

Use the observations from the cherry-picked VA pairs to write a vision
paper for DeepTest 2024 workshop (co-located with ICSE 2024).

I also need to write a paper for CAIN DS 2024.
# Fri Nov 24, 2023

## SERG retreat feedback

-   assertion not clearly defined?
-   all this is done by first author? how do we avoid positive bias?
    -   get a TA to double check the VA pairs (test for sample size)
-   why were the 34 chosen? and how many capture all the information?
-   \"paints a negative picture\": change the tone to not be so
    negative?
-   when is a library popular? some explanation on this. \"based on the
    author\'s knowledge, we limit to the following libraries...\"
-   explain why only Python
-   clarify that Jupyter notebook IS computational notebook
-   intro second paragraph needs reference
-   internal structure of NB is not required?
-   explain why we chose 10 lines to limit the length of the cell?
-   listing 8 typo: \"argmix\" -\> \"argmin\"
-   when did this pattern of testing start?
-   give a motivational example in the introduction! compare and
    contrast with traditional example
-   title of paper is very generic: make it specific to Python and
    Jupyter Notebook
