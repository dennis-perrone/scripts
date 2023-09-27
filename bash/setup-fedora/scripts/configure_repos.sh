#!/bin/bash

# Variables
rpmfusion_base="https://mirrors.rpmfusion.org"
rpmfusion=("free" "nonfree")
repos=$(ls repositories/)

# Configure RPM Fusion repositories
for i in ${rpmfusion[@]}; do
    dnf install -y $rpmfusion_base/$i/fedora/rpmfusion-$i-release-$(rpm -E %fedora).noarch.rpm
done

# Set up other repositories
for i in ${repos[@]}; do
    cat repositories/$i > /etc/yum.repos.d/$i
done