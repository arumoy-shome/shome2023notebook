#!/usr/bin/env bash

if [[ -z "$1" ]]; then
  echo "filter-strict-max-lines-10:ERROR: did not provide valid directory containing notebooks."
  exit 1
fi

if [[ ! -d "$1" ]]; then
  echo "filter-strict-max-lines-10:ERROR: $1 is not a valid directory."
  exit 1
fi

find "$1" -name '*.csv' -print0 |
  xargs -0 -n 1 -P 0 python bin/filter.py --strict --max-num-lines 10
