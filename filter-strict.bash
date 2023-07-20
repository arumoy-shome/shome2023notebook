#!/usr/bin/env bash

( find data/assert_notebooks -name '*.csv' -print0 |
  xargs -0 -n 1 -P 0 python filter.py --strict
)>filter-strict.log 2>filter-strict-error.log
