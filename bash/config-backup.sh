#!/bin/bash

####################################################################
# Script Name : config-backup.sh
# Description : Backs up configuration files to external USB.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

BACKDIR=$HOME/backups
#USBDIR=/run/media/$USER/USB-DISK/linux-backups
#USBDIR=/mnt/usbstick/linux-backups
USBDIR=/media/usb/linux-configuration-backups
DATE=`date +%Y%m%d`

backup_directories(){
    if [[ ! -d $HOME/backups/config-backups ]]; then
        mkdir -p $HOME/backups/config-backups
        mkdir -p $USBDIR/config-backups
#        echo "created directory"
    fi

    if [[ ! -d $HOME/backups/cron-backups ]]; then
        mkdir -p $HOME/backups/cron-backups
        mkdir -p $USBDIR/cron-backups
#        echo "created directory"
    fi

    if [[ ! -d $HOME/backups/taskwarrior-backups ]]; then
        mkdir -p $HOME/backups/taskwarrior-backups
        mkdir -p $USBDIR/taskwarrior-backups
#        echo "created directory"
    fi

    if [[ ! -d $HOME/backups/vimwiki-backups ]]; then
        mkdir -p $HOME/backups/vimwiki-backups
        mkdir -p $USBDIR/vimwiki-backups
#        echo "created directory"
    fi

}

function config_backup() {
#    cd $HOME && tar -czpf $BACKDIR/config-backups/config-$DATE.tar.gz -C $HOME/ {.tmux.conf,.config/hexchat/}
    cd $HOME && tar -czpf $BACKDIR/config-backups/vim-$DATE.tar.gz -C $HOME/ .vim/
    cd $HOME && tar -czpf $BACKDIR/config-backups/bash-$DATE.tar.gz -C $HOME {.bash_profile,.bashrc}
    more /etc/hosts > $BACKDIR/config-backups/host-file-$DATE.bak
    cp $BACKDIR/config-backups/{config,vim,bash}-$DATE.tar.gz $USBDIR/config-backups/
    cp $BACKDIR/config-backups/host-file-$DATE.bak $USBDIR/config-backups/

}

function cron_backup() {
    crontab -l > $BACKDIR/cron-backups/crontab-$DATE.bak
    cp $BACKDIR/cron-backups/crontab-$DATE.bak $USBDIR/cron-backups/

}

function vimwiki_backup() {
    cd $HOME && tar -czpf $BACKDIR/vimwiki-backups/vimwiki-$DATE.tar.gz -C $HOME/ vimwiki/{personal-md,work-md}
    cp $BACKDIR/vimwiki-backups/vimwiki-$DATE.tar.gz $USBDIR/vimwiki-backups/

}

function taskwarrior_backup() {
    cd $HOME && tar -czpf $BACKDIR/taskwarrior-backups/task-rc-$DATE.tar.gz -C $HOME/ .taskrc
    cd $HOME && tar -czpf $BACKDIR/taskwarrior-backups/task-data-$DATE.tar.gz -C $HOME/ .task/
    cp $BACKDIR/taskwarrior-backups/{task-rc,task-data}-$DATE.tar.gz $USBDIR/taskwarrior-backups/

}

backup_directories
config_backup
cron_backup
vimwiki_backup
taskwarrior_backup

