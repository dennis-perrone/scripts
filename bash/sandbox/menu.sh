#!/bin/bash

####################################################################
# Script Name : menu.sh
# Description : Used to test a simple menu
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################


echo "1.) technology"
echo "2.) business"
echo "3.) devops"
read -p "Please select a topic: " topic

if [[ $topic -eq 1 ]]; then
    echo "The topic is technology"
elif [[ $topic -eq 2 ]]; then
    echo "The topic is business"
elif [[ $topic -eq 3 ]]; then
    echo "The topic is devops"
else
    echo "Please select a valid option."
    exit 1
fi



