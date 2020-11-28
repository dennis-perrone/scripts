#!/usr/bin/python3

####################################################################
# Script Name : directory-test.py
# Description : A script to learn a little bit more with how Python
#               searches for paths and directories.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

from pathlib import Path
import os

home = str(Path.home())
dir_path = f"{home}/development/projects/python/taskwarrior/test"



Path(f"{dir_path}").mkdir(parents=True, exist_ok=True)

subfolders = ['sources', 'findings']
subfiles = ['file-01.md', 'file-02.md']
for subfolder in subfolders:
    os.makedirs(os.path.join(f'{dir_path}', subfolder))
    for subfile in subfiles:
        os.mknod(os.path.join(f'{dir_path}', subfolder, subfile))

#print (home)
#print (dir_path)
