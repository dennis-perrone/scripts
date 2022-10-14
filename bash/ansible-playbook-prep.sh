#!/bin/bash

# =========================================================
# Author:  Dennis Perrone
# Github:  https://www.github.com/dennis-perrone
# Purpose: Create a skeleton Ansible playbook.
# =========================================================

# =========================================================
# Variables
# =========================================================
playbook_dir=$HOME/documents/ansible/playbooks
roles_dir=$playbook_dir/$playbook_name/roles
role_var=()
inventory_files=("staging" "production")
main_files=("site.yml")


echo ""
read -p "Please enter the playbook name: " playbook_name
echo ""

if [[ -d $playbook_dir/$playbook_name ]]; then
    echo "Playbook named $playbook_name already exists"
    exit
else
    mkdir -p $playbook_dir/$playbook_name/roles
fi

echo "Please enter the desired role name (Press [ENTER] to exit): "
while true ; do
# This while loop will keep looping while asking for the role variable while
# appending it to an array. Once blank, it will exit out.
    read -p "Enter role: " role
    
    if [[ -z "$role" ]]; then
        break
    fi

    role_var+=($role)
    
done

for i in "${role_var[@]}"; do
    ansible-galaxy init "$playbook_dir/$playbook_name/roles/$i"
done

echo "Created ${#role_var[@]} role(s)."

for i in "${inventory_files[@]}"; do
    echo "# This is the $i inventory file" >> $playbook_dir/$playbook_name/$i
done

for i in "${main_files[@]}"; do
    echo "---" >> $playbook_dir/$playbook_name/$i
    echo "" >> $playbook_dir/$playbook_name/$i
    echo "" >> $playbook_dir/$playbook_name/$i
    echo "-name: " >> $playbook_dir/$playbook_name/$i
done

echo ""
echo "The playbook creation script completed successfully."
echo "The $playbook_name playbook was created successfully."
echo ""
