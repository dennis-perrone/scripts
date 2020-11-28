#!/bin/bash

####################################################################
# Script Name : 
# Description : The purpose of this script is to list all contents
#               in a directory.
# Args : Needs $1 and $1 in order to work properly.
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

#TODO:
# Add error message if there are less than 2 arguments.

location=$1
filename=$2

ls $location > $filename
echo "Script is complete and has indexed the $location."
echo "##########"
echo "Displaying contents of $filename."
echo "##########"
cat $filename
