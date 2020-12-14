#!/bin/bash

####################################################################
# Script Name : array-test.sh
# Description : Used to test functionality and display of arrays
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

read -p "Please enter tags (separated by comma): " blogtags

echo ${blogtags[*]}

for f in ${blogtags[@]}; do
    [[ -f "./$f" ]] || echo "$f: not found"
done
