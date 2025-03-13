ORIGINAL = report/emse24.tex
REVISED = report/emse24-revised.tex
DIFF = report/emse24-diff.tex
RESPONSE = report/emse24-response.tex

all: $(REVISED).pdf $(DIFF).pdf

$(REVISED).pdf: $(REVISED)
	tectonic --synctex $(REVISED)

$(DIFF).pdf: $(DIFF)
	tectonic --synctex $(DIFF)

$(DIFF): $(REVISED) $(ORIGINAL)
	latexdiff $(ORIGINAL) $(REVISED) >$(DIFF)

clean:
	rm -f *.aux *.log *.out *.pdf $(DIFF)

.PHONY: all clean
