#!/bin/bash

####################################################################
# Script Name : clone-git-repos.sh
# Description : Clones git repositories for new box setup.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

# TODO:
# Need to update variables for email address.

#GIT=https://www.github.com
GIT=git@github.com
GITUSER=dennis-perrone
REPODIR=$HOME/development
#REPODIR=$HOME/test

########################################
# Setup git global settings
########################################
#echo "Setting git global settings ..."
#git config --global user.name $GITUSER
#git config --global user.email $GITUSER@gmail.com
#echo "Global git settings have been configured"

########################################
# Clone directories
########################################
repos="ansible dot-files vimwiki scripts projects task-warrior"
for i in $repos
do
    git clone $GIT:$GITUSER/$i $REPODIR/$i
done
