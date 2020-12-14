#!/bin/bash

####################################################################
# Script Name : blog-post.sh
# Description : Creates a template blog post with association to
#               specific blog topic.
# Args : $1 for blog topic (ex. tech, business)
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

dpost=$(date '+%Y-%m-%d %H:%M:%S %z')
dout=$(date '+%Y-%m-%d')

if [[ $# -eq 0 ]]; then
    read -p "Please define the blog posts filename with dashses and no extension (ex. first-post): " filename
    echo "Blog Topics"
    echo "-----------"
    echo "1.) personal"
    echo "2.) tech"
    read -p "Please select the blog posts topic [1-2]: " blogtopic
    if [[ $blogtopic -eq 1 ]]; then
        blogtopic="personal"
    elif [[ $blogtopic -eq 2 ]]; then
        blogtopic="tech"
    else
        echo "Please select a valid topic."
        exit 1
    fi
    read -p "What is the blog posts title?: " blogtitle
    #exit 1
elif [[ $# -eq 1 ]]; then
    filename=$1
    echo "Blog Topics"
    echo "-----------"
    echo "1.) personal"
    echo "2.) tech"
    read -p "Please select the blog posts topic [1-2]: " blogtopic
    if [[ $blogtopic -eq 1 ]]; then
        blogtopic="personal"
    elif [[ $blogtopic -eq 2 ]]; then
        blogtopic="tech"
    else
        echo "Please select a valid topic."
        exit 1
    fi
    read -p "What is the blog posts title?: " blogtitle
else
    echo "Please check file name and use dashes (-) instead of spaces for file name."
    exit 1
fi

<<<<<<< HEAD
blogfinal=$HOME'/development/blog/_posts/'$blogtopic'/'
blogdraft=$HOME'/development/blog/_drafts/'

#cat > "$blogdir/$dout-$filename.md" << EOF
cat > "$blogdraft/$dout-$filename.md" << EOF
=======
finalblog=$HOME'/development/blog/_posts/'$blogtopic'/'
draftblog=$HOME'/development/blog/_drafts/'$blogtopic''

cat > "$draftblog/$dout-$filename.md" << EOF
>>>>>>> 61d29019237b270ad378119c715a55ce5aa27ed8
---
layout: single
title:   "$blogtitle"
date:    $dpost
category: $blogtopic
tags: [ ]
author: Dennis Perrone
---

EOF

