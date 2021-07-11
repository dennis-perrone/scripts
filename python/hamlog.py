#!/usr/bin/python

####################################################################
# Script Name : hamlog.py
# Description : This is intended to be the first draft of a logger
#               for ham radio. It will save the files as a tabbed csv
#               and format in adif. It will also eventually act as a
#               CLI logging program that will ideally log everything
#               in a flat file without needing an extra database.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys
from datetime import date
from pathlib import Path

home = str(Path.home())
config_dir = f'{home}/.config'
date = date.today().isoformat()

# write config files to .config/hamlog/hamlog.conf
# write log files to /var/log/hamlog.log

print (home)
print (config_dir)