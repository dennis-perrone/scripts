#!/bin/bash

####################################################################
# Script Name : ansible-create-playbook.sh
# Description : Creates an Ansible playbook skeleton.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

# TODO:
# Add option to add roles wanted instead of hard coding common

###########################################################
# F U N C T I O N S
###########################################################
ANSIBLE_DIR=$HOME/documents/ansible/playbooks
echo ""
read -p "Enter the desired playbook name: " ANSIBLE_PLAYBOOK
echo ""
ANSIBLE_WORKING_DIR=$ANSIBLE_DIR/$ANSIBLE_PLAYBOOK
ROLES_DIRS=$ANSIBLE_WORKING_DIR/roles
ROLES_FILES=$ROLES_DIRS/common/


if [[ -d $ANSIBLE_WORKING_DIR ]]; then
    echo "Playbook with that name already exists"
else
    mkdir -p $ANSIBLE_WORKING_DIR
fi

if [[ -d $ANSIBLE_WORKING_DIR ]]; then
    mkdir -p $ANSIBLE_WORKING_DIR/{group_vars,host_vars,library,module_utils,filter_plugins,roles}
else
    echo "Failed to create directories"
fi

if [[ -d $ROLES_DIRS ]]; then
    mkdir -p $ROLES_DIRS/common/{tasks,handlers,templates,files,vars,defaults,meta,library,module_utils,lookup_plugins}
    touch $ANSIBLE_WORKING_DIR/{production,staging,site.yml} $ROLES_FILES/{tasks,handlers,templates,files,vars,defaults,meta}/main.yml
else
    echo "No roles directory exists."
fi

echo ""
echo "Script completed successfully."
echo "The $ANSIBLE_PLAYBOOK playbook was created successfully."
echo ""
