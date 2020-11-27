#!/usr/bin/python

import os

playbook_name = input('New playbook name: ')
playbook = "/home/sparky/documents/ansible/playbooks/" + playbook_name


os.makedirs(playbook)
os.chdir(playbook)

main_folders = ['group_vars', 'host_vars', 'library', 'module_utils',
                'filter_plugins', 'roles']
role_folders = ['common', 'web-server', 'db-server']
sub_folders = ['tasks', 'handlers', 'templates', 'files', 'vars', 'defaults',
               'meta', 'library', 'module_utils', 'lookup_plugins']
files = ['production', 'staging', 'site.yml', 'hosts']
role_files = ['main.yml']


for main_folder in main_folders:
    os.makedirs(os.path.join(playbook, main_folder))

for role_folder in role_folders:
    os.makedirs(os.path.join('roles', role_folder))
    for sub_folder in sub_folders:
        os.makedirs(os.path.join('roles', role_folder, sub_folder))
        for role_file in role_files:
            os.mknod(os.path.join('roles', role_folder, sub_folder, role_file))

for file in files:
    os.mknod(file)
