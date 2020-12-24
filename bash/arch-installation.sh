#!/bin/bash

####################################################################
# Script Name : arch-instllation.sh
# Description : A script to automate the installation of Arch Linux.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

# TODO
# Add options for VM set up (30GB of storage) or bare metal (250GB of storage)
# Assume the disk for 

connectivity=$(ping -c 1 8.8.8.8 > /dev/null && echo "up" || echo "down")
disk=$(lsblk --nodeps -no name)

if [[ $connectivity == "up" ]]; then
    echo "Internet connectivity check ... passed ..."
else
    echo "Check your internet connection"
    exit
fi

echo ""
echo "Installaion Type"
echo "----------------"
echo "1.) Virtual Machine (VM)"
echo "2.) Bare Metal"
echo ""
read -p "Please select the installation type: " installtype

if [[ $installtype -eq 1 ]]; then
    echo "Place hdd provisioning"
elif [[ $installtype -eq 2 ]]; then
    echo "Please hdd provisioning for base metal"
else
    echo "Please select a valid option."
    exit
fi

readarray -t lines < <(lsblk --nodeps -no name)
echo ""
echo "Please select a drive: "
select choice in "${lines[@]}"; do
    [[ -n $choice ]] || { echo "Please select a valid choice." >&2; continue; }
    break
done
read -r id <<<"$choice"
echo $id

