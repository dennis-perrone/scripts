#!/usr/bin/python3

import os
import sys
date = '20210601'
#from git import Repo

if __name__ == '__main__':
    #s = sys.argv[1]
    #file_ext = s.split('.')
    #print (file_ext[1])
    gh_site = "https://www.github.com/dennis-perrone"
    os.system(f'git clone {gh_site}/test-repo.git ~/downloads/test-repo')
    os.system(f'cd ~/downloads/test-repo')
    #os.chdir(f'~/downloads/test-repo')
    os.system(f'git checkout -b {date}')