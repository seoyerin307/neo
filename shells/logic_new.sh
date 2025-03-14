#!/bin/bash

opt=$1
opt=$2

if [ $# -eq 2 ];then
    if [ $opt1 == 'test' -a $opt2 == 'aaa' ]; then
        echo good
    elif [ $opt1 == 'aaa' -a $opt2 == 'aaa' ]; then
        echo great
    else
        echo bad
    fi
else
    echo "Input two paramters...!"
fi