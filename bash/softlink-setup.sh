#!/bin/bash

####################################################################
# Script Name : softlink-setup.sh
# Description : Sets up softlinks from development directory for a
#               new installation.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

####################################################################
# Variables
####################################################################
DOC_DIR=$HOME/documents
GIT_DIR=$HOME/development
DOT_DIR=$GIT_DIR/dot-files
PROGRAMMING_DIR=$HOME/programming
VIMWIKI_DIR=$HOME/vimwiki
####################################################################

function config_links {

if [[ ! -h $HOME/.bashrc ]]; then
    ln -s $DOT_DIR/bash-configs/bashrc $HOME/.bashrc
    echo "bashrc link is created."
elif [[ ! -h $HOME/.bash_profile ]]; then
    ln -s $DOT_DIR/bash-configs/bash_profile $HOME/.bash_profile
    echo "bash_profile link is created."
#elif [[ ! -h $HOME/.tmux.conf ]]; then
#    ln -s $DOT_DIR/tmux-configs/tmux.conf-20200301 $HOME/.tmux.conf
#    echo "tmux config link is created."
#elif [[ ! -h $HOME/,config/i3 ]]; then
#    ln -s $DOT_DIR/i3-configs/ $HOME/.config/i3
#    echo "i3 config link is created."
else
    echo "link is already created."
fi

}

####################################################################

function ansible_link {

if [[ ! -h $DOC_DIR/ansible ]]; then
    ln -s $GIT_DIR/ansible $DOC_DIR/ansible
    echo "ansible link is created."
else
    echo "link is already created."
fi

}

####################################################################

function programming_links {

if [[ !"$(ls -A $PROGRAMMING_DIR)" ]]; then
    ln -s $GIT_DIR/projects/python $PROGRAMMING_DIR/python
    ln -s $GIT_DIR/scripts/bash $PROGRAMMING_DIR/bash
    ln -s $GIT_DIR/scripts/powershell $PROGRAMMING_DIR/powershell
    echo "links for python, bash, and powershell created."
else
    echo "links already created."
fi

}

####################################################################

function vim_link {

if [[ ! -h $HOME/.vim ]]; then
    ln -s $DOT_DIR/vim-configs/.vim-20200301 $HOME/.vim
    echo "vim config link is created."
else
    echo "link is already created."
fi

}

####################################################################

function vimwiki_links {

if [[ !"$(ls -A $VIMWIKI_DIR)" ]]; then
    ln -s $GIT_DIR/vimwiki/personal-md $VIMWIKI_DIR/personal-md
    ln -s $GIT_DIR/vimwiki/work-md $VIMWIKI_DIR/personal-md
    echo "links for vimwikis are created."
else
    echo "links already created."
fi

}

####################################################################

config_links
ansible_link
programming_links
vim_link
#vimwiki_links
