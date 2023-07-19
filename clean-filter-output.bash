#!/usr/bin/env bash

# clean up the output from filter.py script.
# args:
# $0: in (name of input log file)
# $1: out (name of output log file)

# exit after first error
set -o errexit

# delete the carret-returns at the end of each line, super weird that
# this exists in a unix container?

tr -d '\r' |
# remove lines that are not notebooks (remove the errors)
grep 'ipynb$' | 
# sort the names
sort
