# Building PDF files

All latex source files are located inside the `report/` directory. You can use the `latexmk` command (included in the full distribution of LaTeX) to build the PDF document.

```
cd report/
latexmk -pdf --synctex=1 -f emse24.tex
```

Alternatively, if you don't want to install the entire tex distribution, you can use the `tectonic` <https://tectonic-typesetting.github.io/en-US/> command to build the PDF.

```
tectonic --synctex report/emse24.tex
```

# Generating diff documents

Use the `latexdiff` command to create a tex file that shows the difference between two latex files.

``` bash
latexdiff old.tex new.tex >diff.tex
```

# EMSE document changelog
1. report/emse24.tex: this is the original EMSE submission
2. report/emse24-revised.tex: this is the revised version (resubmitted to EMSE)
3. report/emse24-response.tex: this is the response document for the first round of reviews (received on emse24.tex)
4. report/emse24-diff.tex: diff between emse24.tex and emse24-revised.tex
