#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file1.tex> <file2.tex>"
    exit 1
fi

FILE1=$1
FILE2=$2
DIFF_FILE="diff.tex"

# Expand LaTeX files (in case they use \input or \include)
latexpand "$FILE1" > old.tex
latexpand "$FILE2" > new.tex

# Generate the diff file using latexdiff
latexdiff old.tex new.tex > "$DIFF_FILE"

# Compile the diff.tex file to generate the PDF
latexmk -pdf -f "$DIFF_FILE"

# Clean up temporary files
rm old.tex new.tex "$DIFF_FILE"

echo "PDF diff generated successfully!"
