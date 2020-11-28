#!/bin/bash

####################################################################
# Script Name : backup-clean.sh
# Description : Cleans up local backup directory of files older
#               than specified days.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

BACK_DIR="$HOME/backups"
#USB_DIR="/mnt/usbstick/linux-backups/"
USB_DIR="/run/media/$USER/USB-DISK/linux-backups/"

#find $BACK_DIR -mtime +7 -type f -delete

if [[ -d $USB_DIR ]]; then
    find $BACK_DIR -mtime +7 -type f -delete
    find $USB_DIR -mtime +7 -type f -delete
else
    find $BACK_DIR -mtime +7 -type f -delete
fi

########################################
# Use the below to test functionality
########################################
#find $BACK_DIR -type f -delete
