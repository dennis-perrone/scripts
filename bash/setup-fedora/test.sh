#!/bin/bash

#declare -a test_arr
# repos=$(ls repositories/)

# declare -a test_arr
# test_arr=($repos)


# for i in ${test_arr[@]}; do
#   echo "Repo: $i"
# done

repos=$(ls repositories/)
for i in ${repos[@]}; do
    echo $i
done