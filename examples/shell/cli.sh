#!/bin/bash

function args()
{
    options=$(getopt -o dv --long debug --long name: -- "$@")
    [ $? -eq 0 ] || {
        echo "Incorrect option provided"
        exit 1
    }
    eval set -- "$options"
    while true; do
        case "$1" in
        -v)
            VERBOSE=1
            ;;
        -d)
            DEBUG=1
            ;;
        --debug)
            DEBUG=1
            ;;
        --name)
            shift; # The arg is next in position args
            NAME=$1
            ;;
        --)
            shift
            break
            ;;
        esac
        shift
    done
}

args $0 "$@"

echo $NAME
echo $DEBUG
echo $VERBOSE


