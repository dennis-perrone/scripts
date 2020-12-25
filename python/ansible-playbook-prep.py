#!/usr/bin/python3

####################################################################
# Script Name : ansible-playbook-prep.py
# Description : A simple script to create a skelton playbook and the
#               desired roles.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys

if os.geteuid() == 0:
    sys.exit ("This sript should not be executed as root.\n"
              "Please re-run this script as a normal user.")

playbook_dir = os.environ['HOME'] + "/development/ansible/playbooks/"
playbook_name = input('Please enter then playbook name: ')
playbook = playbook_dir + playbook_name

if not os.path.exists(playbook):
    os.makedirs(playbook)
    os.chdir(playbook)
    print (f'Playbook ' + playbook_name + ' has been created.')
else:
    print (f'The playbook ' + playbook_name + ' already exists.')

main_folders = ['group_vars', 'host_vars', 'library', \
                'module_utils', 'filter_plugins', 'roles']
roles = []
inventory = ['production', 'staging']
files = ['site.yml']

for m in main_folders:
    os.makedirs(os.path.join(playbook, m))

for f in inventory:
    os.mknod(f)
    file = open(f,"w+")
    filecontent = ["# This is the " + f + " inventory file.\n\n"]
    file.writelines(filecontent)
    file.close()

for f in files:
    os.mknod(f)
    file = open(f,"w+")
    filecontent = ["---\n\n"]
    file.writelines(filecontent)
    file.close()

os.chdir(playbook + '/roles/')

while True:
    print ()
    print ('Please enter the desired role name (Press [ENTER] to exit): ')
    role = input()
    if role == '':
        break
    roles = roles + [role]
print ('The following roles were created : ')
for i in roles:
    os.system('ansible-galaxy init ' + i)

