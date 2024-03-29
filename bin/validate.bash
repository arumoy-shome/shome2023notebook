#!/usr/bin/env bash

set -euo pipefail
set -x

find data/assert_notebooks -name '*.ipynb' -not -path '*ipynb_checkpoints*' -print0 |
# find data/mondal2023cell2doc/Cell2Doc-Artifacts/Repository/notebooks-dataset/notebooks -name '*.ipynb' -not -path '*ipynb_checkpoints*' |
# find data/quaranta2021kgtorrent/KT_dataset -name '*.ipynb' -not -path '*ipynb_checkpoints*' -print0 |
# find data '*.ipynb' -not -path '*ipynb_checkpoints*' |
  # shuf -n 10 |
  # tr '\n' '\0' |
  # test first with a sample print to check find output is as expected
  # xargs -0 -n 1 -P 0 # xargs uses echo by default
  # and finally run the full command
  xargs -0 -n 1 -P 0 python bin/validate.py
