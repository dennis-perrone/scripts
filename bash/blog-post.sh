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

function topic_choice(){
    echo ""
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
}

function post_stage(){
    echo ""
    echo "Blog Stage"
    echo "----------"
    echo "1.) staging (_drafts)"
    echo "2.) production (_posts)"
    read -p "Please select the post stage [1-2]: " blogstage
    if [[ $blogstage -eq 1 ]]; then
        blogstage="_drafts"
    elif
        [[ $blogstage -eq 2 ]]; then
        blogstage="_posts"
    else
        echo "Please select a valid blog stage"
        exit
    fi
}

function blog_header(){

cat > "$HOME/development/blog/$blogstage/$blogtopic/$dout-$filename.md" << EOF
---
layout: single
title:   "$blogtitle"
date:    $dpost
category: $blogtopic
tags: [ ]
author: Dennis Perrone
classes: wide
---

EOF

}

if [[ $# -eq 0 ]]; then
    read -p "Please define the blog posts filename with dashses and no file extension (ex. first-post): " filename
    post_stage
    topic_choice
    read -p "What is the blog posts title?: " blogtitle
    blog_header
elif [[ $# -eq 1 ]]; then
    filename=$1
    post_stage
    topic_choice
    read -p "What is the blog posts title?: " blogtitle
    blog_header
else
    echo "Please check file name and use dashes (-) instead of spaces for file name."
    exit 1
fi
