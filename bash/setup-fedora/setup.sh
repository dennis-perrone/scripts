#!/bin/bash

# Configure system repositories
echo "Configuring repositories ..."
source ./scripts/configure_repos.sh

# Update system and install desired packages
echo "Updating system packages and installing desired software ..."
source ./scripts/dnf_install.sh

# Set up Flatpak
echo "Configuring and updating Flatpaks ..."
source ./scripts/flatpak_install.sh

# Configure Gnome
echo "Installing Gnome extensions ..."
source ./scripts/gnome_extensions.sh

echo "Configuring Gnome settings ..."
source ./scripts/gnome_settings.sh"