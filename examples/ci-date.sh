#!/bin/bash
tmp_dir=$(mktemp -d -t ci-$(date +%Y-%m-%d-%H-%M-%S)-XXXXXXXXXX)

echo $tmp_dir

rm -rf $tmp_dir
