#!/usr/bin/env bash

set -euo pipefail
set -x

# mondal2023cell2doc
## mondal2023cell2doc-stats.csv
(
find data/shome2023notebook/mondal2023cell2doc -name '*-stats.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/mondal2023cell2doc-stats.csv

## mondal2023cell2doc-assert-content.csv
(
find data/shome2023notebook/mondal2023cell2doc -name '*-assert-content.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/mondal2023cell2doc-assert-content.csv

## mondal2023cell2doc-assert-context.csv
(
find data/shome2023notebook/mondal2023cell2doc -name '*-assert-context.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/mondal2023cell2doc-assert-context.csv

## mondal2023cell2doc-outputs.csv
(
find data/shome2023notebook/mondal2023cell2doc -name '*-outputs.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/mondal2023cell2doc-outputs.csv

# quaranta2021kgtorrent
## quaranta2021kgtorrent-stats.csv
(
find data/shome2023notebook/quaranta2021kgtorrent -name '*-stats.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/quaranta2021kgtorrent-stats.csv

## quaranta2021kgtorrent-assert-content.csv
(
find data/shome2023notebook/quaranta2021kgtorrent -name '*-assert-content.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/quaranta2021kgtorrent-assert-content.csv

## quaranta2021kgtorrent-assert-context.csv
(
find data/shome2023notebook/quaranta2021kgtorrent -name '*-assert-context.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/quaranta2021kgtorrent-assert-context.csv

## quaranta2021kgtorrent-outputs.csv
(
find data/shome2023notebook/quaranta2021kgtorrent -name '*-outputs.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/quaranta2021kgtorrent-outputs.csv

# Github
## github-stats.csv
(
find data/shome2023notebook/assert_notebooks -name '*-stats.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/github-stats.csv

## github-assert-content.csv
(
find data/shome2023notebook/assert_notebooks -name '*-assert-content.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/github-assert-content.csv

## github-assert-context.csv
(
find data/shome2023notebook/assert_notebooks -name '*-assert-context.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/github-assert-context.csv

## github-outputs.csv
(
find data/shome2023notebook/assert_notebooks -name '*-outputs.csv' -print0 |
xargs -0 -n 1 cat
)>data/shome2023notebook/github-outputs.csv
