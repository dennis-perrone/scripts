#!/bin/bash

####################################################################
# Script Name : check-diskspace.sh
# Description : Checks diskspace with different thresholds
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

DISKSPACE=$(df -P / | tail -1 | awk '{print $5}' | tr -d "%")
case $DISKSPACE in
    100)
        echo "The disk is full."
        echo "Emergency! Disk is full!" | mail -s "Disk emergency" dennis.perrone@gmail.com
        ;;
    [1-7]*[0-9])
        echo "Lots of space left, the disk is currently $DISKSPACE% full."
        ;;
    [8-9]*)
        echo "I am at least 80% full."
        ;;
    *)
        echo "Hmm, I expected to see some kind of percentage."
esac
