#!/usr/bin/python3

import os
import sys
import git
from git import Repo
from pathlib import Path
from datetime import date


date = date.today().isoformat()
home = str(Path.home())
repo = git.Repo('test-repo')
#repo = git.Repo(f'{home}/development/notes')

if __name__ == '__main__':

    #if os.path.isdir("/home/sparky/downloads/test-repo/"):
    #    print ("The repository has already been cloned.")
    #else:
    #    git.Repo.clone_from('git@github.com:dennis-perrone/test-repo', 'test-repo')
    repo = git.Repo('test-repo')

    if repo.is_dirty(untracked_files=True):
        print ("Changes detected")
        repo.index.add(['test03.txt'])
        repo.index.commit('Updated documentation')
    else:
        print ("All clean")

    for branch in repo.branches:
        print (branch)
    
    repo.git.checkout('main')
    repo.git.branch(f'{date}')
    repo.git.checkout(f'{date}')
    #main = self.repo.heads.main
    #repo.git.pull('origin', 'main')
    repo.git.push('--set-upstream', 'origin', f'{date}')
    repo.git.pull('origin', 'main')
    repo.git.checkout('main')



    
    #git@github.com:dennis-perrone/test-repo.git