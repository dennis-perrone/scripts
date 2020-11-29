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
    echo "Please enter the title for the blog post."
    exit 1
fi

cat > "$dout-$1.md" << EOF
---
layout: post
title: 
date:   $dpost
category: 
---

EOF
