# Annotations process
This section documents the annotation process that was followed.
1. In the max-lines-10 sheet, we check if the visualisation-assertion pair(s) are related to each other or not. And annotate the patterns for RQ2.
2. NBs that make it though this pass get transferred to the select sheet where:
    1. We analyse them in more detail, specifically we note down observations regarding the visualisation and assertion (together and individually)
    2. In the event that we find a notebook was mis-classified (ie. It shouldn’t have been selected, we go back and update the max-lines-10 sheet and delete it from the select sheet

# Building 

Use the following command to build the paper (assuming you have the full latex distribution installed locally on your computer):

```{.bash}
cd report/
latexmk -pdfxe esecfse24.tex
```
