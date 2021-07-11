#/usr/bin/python3

####################################################################
# Script Name : convert-docs.py
# Description : Utilizes pandoc to convert between two file types.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys
import shutil
import getpass
import git
from pathlib import Path
from git import Repo
from datetime import date

current_user = getpass.getuser()
home = str(Path.home())
repo = git.Repo(f'{home}/development/notes')
date = date.today().isoformat()

if len(sys.argv) <= 1:
    print (f"Execute this command with the following arguments:")
    print (f"python3 {sys.argv[0]} <input file name>.extension")
    sys.exit(1)

def main():
    file_in()
    file_out()
    os.system(f'pandoc -f {file_ext} -t {ext} -o {file_name}.md {sys.argv[1]}')
    source = f"/home/{current_user}/downloads/{file_name}.md"
    research_topic()
    if not os.path.exists(f"{home}/development/notes/{topic}/{cert}/"):
        os.makedirs (f'{home}/development/notes/{topic}/{cert}/')
    des = f"{home}/development/notes/{topic}/{cert}/"
    move = shutil.copy(source, des)
    git_actions()

def research_topic():
    global topic
    global cert
    os.system('cls' if os.name == 'nt' else 'clear')
    print ()
    print (f"What is the research topic")
    print (f"----------------")
    print (f"1.) Certification")
    print (f"2.) Other")
    print ()
    topic = input ("Please select the overall research topic [1-2]: ")
    if topic == "1":
        topic = "certifications"
        print ()
        print ("Certifications")
        print (f"----------------")
        print (f"1.) PMI Project Management Professional (PMP)")
        print (f"2.) Cisco Certified Network Associate (CCNA)")
        print ()
        cert = input ("Choose the certification topic: ")
        print ()
        if cert == "1":
            cert = "pmi-pmp"
        elif cert == "2":
            cert = "cisco-ccna"
        else:
            print ("Please add option for additional certification")
            exit (1)
        source = f"/mnt/c/Users/{current_user}/Documents/{topic}/study/{cert}/{sys.argv[1]}"
        des = f"/home/{current_user}/downloads/"
        move = shutil.copy(source, des)

    elif topic == "2":
        topic = "other"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Please select a valid topic")
        print ("No changes have been made")
        exit(1)

def git_actions():
    if repo.is_dirty(untracked_files=True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Git actions to commit notes to remote repository")
        print (f"----------------")
        print ()
        print (f"Detected that {file_name}.md has been modified ...")
        print ()
        print (f"Adding {file_name} to staging area.")
        print ()
        repo.index.add([f'{topic}/{cert}/{file_name}.md'])
        repo.index.commit(f'Updated {file_name} notes.')
        print (f"Commited {file_name} to the notes repository.")
    else:
        print ("All clean")
    
    repo.git.checkout('main')
    #repo.git.branch(f'{file_name}_notes')
    #repo.git.checkout(f'{file_name}_notes')
    repo.git.pull('origin', 'main')
    #repo.git.push('--set-upstream', 'origin', f'{file_name}_notes')
    repo.git.push('--set-upstream', 'origin', 'main')
    repo.git.pull('origin', 'main')
    #repo.git.checkout('main')

def file_in():
    global file_ext
    global file_name
    ingest = sys.argv[1]
    ingest_ext = ingest.split('.')
    file_name = (ingest_ext[0])
    file_ext = (ingest_ext[-1])

def file_out():
    global ext
    os.system('cls' if os.name == 'nt' else 'clear')
    print ()
    print (f"Markdown Flavors")
    print (f"----------------")
    print (f"1.) Github Markdown")
    print (f"2.) Traditional Markdown")
    print ()
    ext = input ("Please select which flavor of markdown desired for conversion [1-2]: ")
    if ext == "1":
        ext = "gfm"
    elif ext == "2":
        ext = "markdown"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Please select a valid extension")
        print ("No changes have been made")
        exit(1)  

if __name__ == "__main__":
    main()
