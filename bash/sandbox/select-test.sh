#!/bin/bash

####################################################################
# Script Name : select-test.sh
# Description : Used to test functionality of the select function
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

select topic in Business Technology DevOps
do
    echo "Selected Topic:" $topic
    exit 1
done

