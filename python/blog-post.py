#!/usr/bin/python3

####################################################################
# Script Name : blog-post.py
# Description : This script creates a blog post based on input from
#               use input.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys
import datetime
from pathlib import Path
import time

######################################################################
# Terminal Colors
######################################################################
NC='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

######################################################################
# Initial validation steps for script
######################################################################
os.system('cls' if os.name == 'nt' else 'clear')

dpost = time.strftime('%Y-%m-%d %H:%M:%S %z')
dout = time.strftime('%Y-%m-%d')
home = str(Path.home())


def main():
    global post_name
    global post_title
    if len(sys.argv) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        post_name = input(f'Please define the blog posts filename with dashes and no file extension (ex. first-post): ')
        post_category()
        post_stage()
        post_title = input(f'What is the blog posts title?: ')
        post_header()
    elif len(sys.argv) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        post_name = input(f'Please define the blog posts filename with dashes and no file extension (ex. first-post): ')
        post_category()
        post_stage()
        post_title = sys.argv[1]
        post_header()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("You messed up")
        exit ()

def post_category():
    global blogcat
    print ()
    print ("Blog Categories")
    print ("---------------")
    print ("1.) general")
    print ("2.) personal")
    print ("3.) professional")
    print ("4.) technology")
    print ()
    category = input("Please select the blog posts category [1-2]: ")
    if category == "1":
        blogcat = "general"
    elif category == "2":
        blogcat = "personal"
    elif category == "3":
        blogcat = "professional"
    elif category == "4":
        blogcat = "tech"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Please select a valid category")
        print ("No changes have been made")
        exit(1)

def post_stage():
    global blogstage
    print ()
    print ("Blog Post Stage")
    print ("----------------")
    print ("1.) staging (_drafts)")
    print ("2.) production (_posts)")
    print ()
    stage = input(f"Please select the post stage [1-2]: ")
    if stage == "1":
        blogstage = "_drafts"
    elif stage == "2":
        blogstage = "_posts"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Please select a valid category")
        print ("No changes have been made")
        exit(1)

def post_header():
    filename = f'{home}/development/blog/{blogstage}/{blogcat}/{dout}-{post_name}.md'
    f = open(filename,"w+")
    filecontent = ["---\n","layout:   single","\n","title:    ",\
            post_title,"\n","date:     ",dpost,"\n","category: ",\
            blogcat,"\n","tags: [ ]\n","author:   Dennis Perrone\n",\
            "excerpt:  \n","classes:  wide\n","---\n"]
    f.writelines(filecontent)
    f.close()

if __name__ == "__main__":
    main()
