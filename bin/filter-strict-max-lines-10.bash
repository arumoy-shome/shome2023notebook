#!/usr/bin/env bash

( find data/assert_notebooks -name '*.csv' -print0 |
  xargs -0 -n 1 -P 0 python filter.py --strict --max-num-lines 10
)>filter-strict-max-lines-10.log 2>filter-strict-max-lines-10-error.log
