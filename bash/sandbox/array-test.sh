#!/bin/bash

####################################################################
# Script Name : array-test.sh
# Description : Used to test functionality and display of arrays
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

array=(1,2,3)
read -p "Please enter tags (separated by comma): " blogtags

echo ${array[*]}
echo ${blogtags[*]}
