#!/bin/bash

####################################################################
# Script Name : directory-check.sh
# Description : Checks to see if a directory is created.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

echo "Hello, $USER!"
echo "Which directory would you like to check? Use absolute path."
read dirpath
if [[ -d $dirpath ]]; then
    echo "Directory exists.";
    else
        echo "Directory doesn't exist, would you like to create it? [Y/N] "
        read -n 1 -s makedir
    if [ $makedir == "Y" ]; then
        echo "Creating the new directory."
        mkdir -p $dirpath
    else
        echo "Okay, exiting script now."
        exit 1
    fi
fi
