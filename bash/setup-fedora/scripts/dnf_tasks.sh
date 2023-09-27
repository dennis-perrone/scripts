#!/bin/bash

# Update all packages
dnf upgrade -y --refresh
#dnf groupupdate -y core

# Install packages
dnf install -y $(cat ./vars/package_list_install.txt)

# Uninstall unwanted packages
dnf uninstall -y $(cat ./vars/package_list_uninstall.txt)