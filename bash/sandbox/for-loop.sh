#!/bin/bash

####################################################################
# Script Name : for-loop.sh
# Description : 
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

depts=("it" "hr" "sales")

clear
#echo $depts
#echo ${depts[*]}
echo
echo "Departments Available"
echo "------------------------"
for x in "${depts[@]}"
do
    echo " $x department"
done
echo
