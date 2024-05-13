#!/usr/bin/env bash

# usage: docker run -it --rm -v "$(pwd):/app" shome2023notebook bash bin/filter.bash

# change the base directory as required:
# github: data/assert_notebooks
# cell2doc: data/mondal2023cell2doc/Repository/notebooks-dataset/notebooks
# all: data

find data/assert_notebooks -name '*.ipynb' -not -path '*/ipynb_checkpoints/*' |
find data/mondal2023cell2doc/Repository/notebooks-dataset/notebooks -name '*.ipynb' -not -path '*/ipynb_checkpoints/*' |
# find data '*.ipynb' -not -path '*/ipynb_checkpoints/*' |
  # change the shuf parameter based on sample size
  shuf -n 100 |
  tr '\n' '\0' |
  # test first with a sample print to check find output is as expected
  # xargs -0 -n 1 -P 0 # xargs uses echo by default
  # and finally run the full command
    xargs -0 -n 1 -P 0 python bin/filter.py
