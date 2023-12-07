#!/bin/bash

# Enable window buttons
gsettings set org.gnome.desktop.wm.preferences button-layout ":minimize,maximize,close"

# Set new windows centered
gsettings set org.gnome.mutter center-new-windows true