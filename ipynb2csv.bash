#!/usr/bin/env bash

find data/assert_notebooks -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*' -print0 |
    xargs -0 -n 1 -P 0 python ipynb2csv.py
