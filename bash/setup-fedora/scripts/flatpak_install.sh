#!/bin/bash

# Check if flatpak is enabled on the system
if ! flatpak --version > /dev/null 2>&1; then
  echo "Error: flatpak is not enabled on this system"
  exit 1
fi

# Add remote for Flathub
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Update existing flatpaks
flatpak update

# Read the list of packages from the text file
PACKAGES=$(cat vars/flatpak_list.txt)

# Install the packages using flatpak
for PACKAGE in $PACKAGES; do
  flatpak install -y $PACKAGE
done
