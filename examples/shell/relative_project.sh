#!/bin/bash

project_root=$(dirname $(dirname $(dirname $(realpath $0 ))))
echo $project_root

data_dir="$project_root/examples/data"
echo "DATA: $data_dir"


