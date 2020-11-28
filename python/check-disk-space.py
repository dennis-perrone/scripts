#!/usr/bin/python3

####################################################################
# Script Name : check-disk-space.py
# Description : A simple script to check disk space.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import shutil

def root_space():
    total, used, free = shutil.disk_usage("//")
    print("-------------------------")
    print("Partition: /")
    print("-------------------------")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))
    print("-------------------------")
    print("")


def home_space():
    total, used, free = shutil.disk_usage("/home")
    print("-------------------------")
    print("Partition: /home")
    print("-------------------------")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))
    print("-------------------------")
    print("")


root_space()
home_space()
