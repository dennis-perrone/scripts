#!/bin/python3

####################################################################
# Script Name : rename-publications.py
# Description : A script intended to be ran within a Downloads
#               directory. It should parse and rename all documents
#               to a standard naming convention
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os

# TODO:
# Add variable for download directory
os.chdir('')


def nist():
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_org, f_series, f_num, f_title, = f_name.split(' ', 3)
        f_title_name, f_date = f_title.split(',')
        new_name = ('{}-{}-{}{}'.format(f_org, f_series, f_num, f_ext).lower())
        os.rename(f, new_name)


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_inst = f_name.split('_')
#    f_pub = f_inst.split('')

#    f_pub, f_date = f_inst.split()
    print(f_inst)
