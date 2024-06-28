#!/usr/bin/env bash

set -euo pipefail
set -x

# (
# find data/shome2023notebook/assert_notebooks data/shome2023notebook/quaranta2021kgtorrent -name '*-stats.csv' -print0 |
# xargs -0 -n 1 cat
# )>data/shome2023notebook/stats.csv

# (
# find data/shome2023notebook/assert_notebooks data/shome2023notebook/quaranta2021kgtorrent -name '*-asserts.csv' -print0 |
# xargs -0 -n 1 cat
# )>data/shome2023notebook/asserts.csv

(
find data/shome2023notebook/assert_notebooks data/shome2023notebook/quaranta2021kgtorrent -name '*-outputs.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/outputs.csv
