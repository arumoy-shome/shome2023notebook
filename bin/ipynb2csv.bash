#!/usr/bin/env bash

if [[ -z "$1" ]]; then
  echo "ipynb2csv:ERROR: did not provide valid directory containing notebooks."
  exit 1
fi

if [[ ! -d "$1" ]]; then
  echo "ipynb2csv:ERROR: $1 is not a valid directory."
  exit 1
fi

find "$1" -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*' -print0 |
  xargs -0 -n 1 -P 0 python bin/ipynb2csv.py
