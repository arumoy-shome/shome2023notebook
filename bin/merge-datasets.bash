#!/usr/bin/env bash

set -euo pipefail
set -x

(
find data/anon/assert_notebooks data/anon/quaranta2021kgtorrent -name '*-stats.csv' -print0 |
xargs -0 -n 1 cat
)>data/anon/stats.csv

# (
# find data/anon/assert_notebooks data/anon/quaranta2021kgtorrent -name '*-asserts.csv' -print0 |
# xargs -0 -n 1 cat
# )>data/anon/asserts.csv

# (
# find data/anon/assert_notebooks data/anon/quaranta2021kgtorrent -name '*-outputs.csv' -print0 |
# xargs -0 -n 1 cat
# )>data/anon/outputs.csv
