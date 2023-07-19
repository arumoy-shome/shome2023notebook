#!/usr/bin/env bash

find data/assert_notebooks -name '*.csv' -print0 |
  tr '\0' '\n' |
  head -n 500 |
  tr '\n' '\0' |
  xargs -0 -n 1 -P 0 python filter-proximity.py
