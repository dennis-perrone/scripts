#!/bin/bash

# =========================================================
# Author:  Dennis Perrone
# Github:  https://www.github.com/dennis-perrone
# Purpose: Create distrobox and sandboxed home directories
# =========================================================

if [[ $# -eq 0 ]]; then
    echo "No distrobox name provided"
    read -p "Define the distrobox name: " name
    if [[ -z $name ]]; then
        echo "Unable to determine name for distrobox"
        echo "Exiting script ..."
        exit 1
    fi
else
    name=$1
fi

echo "If selecting a Red Hat image, use the following: "
echo "UBI 8: registry.access.redhat.com/ubi8/ubi"
echo "UBI 9: registry.access.redhat.com/ubi9/ubi"
read -p "Specify which image to use (ex. fedora:36, archlinux:latest, etc.): " image

# Create sandbox home directories
homedir=~/boxes/${name}
if [[ -d ~/boxes/${name} ]]; then
    echo "Directory already exists."
    read -p "Enter the existing distrobox? [Y/N]: " response
    response=${response,,}
    if [[ "$response" =~ ^(yes|y)$ ]]; then
        distrobox enter ${name}
    else
        echo "Exiting the script ..."
        exit 1
    fi
else
    mkdir -p ${homedir}
    distrobox create -n ${name} -i ${image} -H ${homedir}
fi