#!/bin/bash
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
echo $tmp_dir

# ...

rm -rf $tmp_dir

