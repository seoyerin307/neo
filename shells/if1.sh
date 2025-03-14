#!/bin/bash

echo "File Name : $0"
echo "Parameter Count : $#"
echo "All Parametet : $@"

if [ "$1" = ok ];  then
    echo good~!!
else
    echo bad~!!
fi