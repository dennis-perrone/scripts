#!/bin/bash

# Variables
gnome_base="https://extensions.gnome.org/extension"

extensions=( https://extensions.gnome.org/extension/1160/dash-to-panel/ \
https://extensions.gnome.org/extension/4655/date-menu-formatter/
https://extensions.gnome.org/extension/4099/no-overview/
https://extensions.gnome.org/extension/750/openweather/
https://extensions.gnome.org/extension/4548/tactile/
)

for i in ${extensions[@]}; do
    EXTENSION_ID=$(curl -s $i | grep -oP 'data-uuid="\K[^"]+')
    VERSION_TAG=$(curl -Lfs "https://extensions.gnome.org/extension-query/?search=$EXTENSION_ID" | jq '.extensions[0] | .shell_version_map | map(.pk) | max')
    wget -O ${EXTENSION_ID}.zip "https://extensions.gnome.org/download-extension/${EXTENSION_ID}.shell-extension.zip?version_tag=$VERSION_TAG"
    gnome-extensions install --force ${EXTENSION_ID}.zip
    if ! gnome-extensions list | grep --quiet ${EXTENSION_ID}; then
        busctl --user call org.gnome.Shell.Extensions /org/gnome/Shell/Extensions org.gnome.Shell.Extensions InstallRemoteExtension s ${EXTENSION_ID}
    fi
    gnome-extensions enable ${EXTENSION_ID}
    rm ${EXTENSION_ID}.zip
done

# for i in ${extensions[@]}; do
#     EXTENSION_ID=$(curl -s $i | grep -oP 'data-uuid="\K[^"]+')
#     gnome-extensions enable $EXTENSION_ID
# done