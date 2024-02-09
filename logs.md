---
title: shome2023llm logbook
---

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
