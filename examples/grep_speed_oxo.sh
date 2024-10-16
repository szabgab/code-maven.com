#!/bin/bash

if (($# != 2)); then
    echo "$0" 'FILENAME LIMIT' >&2
    exit 1
fi

filename=$1
limit=$2

for ((i=limit; i; --i)); do
    grep '\(.\)y\1' "$filename"
done
