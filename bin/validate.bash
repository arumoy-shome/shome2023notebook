#!/usr/bin/env bash

# change the base directory as required:
# github: data/assert_notebooks
# cell2doc: data/mondal2023cell2doc/Repository/notebooks-dataset/notebooks
# all: data

# find data/assert_notebooks -name '*.ipynb' -not -path '*/ipynb_checkpoints/*' -print0 |
find data/mondal2023cell2doc/Repository/notebooks-dataset/notebooks -name '*.ipynb' -not -path '*/ipynb_checkpoints/*' |
# find data '*.ipynb' -not -path '*/ipynb_checkpoints/*' -print0 |
  shuf -n 100 |
  tr '\n' '\0' |
# find data/assert_notebooks -name '*.ipynb' -not -path '*/ipynb_checkpoints/*' -print0 |
  # test first with a sample print to check find output is as expected
    xargs -0 -n 1 -P 0 python bin/validate.py
    # xargs -0 -n 1 -P 0 # xargs uses echo by default
