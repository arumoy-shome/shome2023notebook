#!/usr/bin/env bash

set -euo pipefail
set -x

find data/assert_notebooks data/quaranta2021kgtorrent -type f -name "*.ipynb" ! -path "*/ipynb_checkpoints/*" -print0 |
# shuf -z |
# head -z -n 500 |
# xargs -0 -n 1 -P 0
xargs -0 -n 1 -P 0 python bin/data-collection-outputs.py
