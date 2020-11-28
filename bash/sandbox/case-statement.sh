#!/bin/bash

####################################################################
# Script Name : case-statement.sh
# Description : 
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

case $1 in
    start)
        echo "Starting the process."
        ;;
    stop)
        echo "Stopping the process."
        ;;
    *)
        echo "I need to hear start or stop."
esac
