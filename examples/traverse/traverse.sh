#!/bin/bash

find $1 -print0 | while IFS= read -r -d '' filename
do
    true
    #echo ": $filename"
done
