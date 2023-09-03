#!/bin/bash

HOST=192.168.1.65
PORT=22
DIRS=("documents" "pictures" "music")

if nc -z $HOST $PORT 2>/dev/null; then
  # Copy main home directory items
  for i in ${DIRS[@]}; do
    rsync -avh --delete /home/$USER/$i/ $USER@$HOST:/home/samba-share/home_dir_files/$i/
  done
  # Copy the KeePassXC database
  rsync -avh --delete /home/$USER/passwords.kdbx $USER@$HOST:/home/samba-share/home_dir_files/
  # Copy virtual machines
  rsync -avh --delete /home/$USER/virtual-machines/ $USER@$HOST:/home/samba-share/home_dir_files/virtual-machines/
  echo "$(date +%Y-%m-%d\ \(%a\)): Successfully completed the scheduled sync to backup." >> /home/$USER/cron-sync-log.txt
else
  echo "$(date +%Y-%m-%d\ \(%a\)): Failed to complete the scheduled sync." >> /home/$USER/cron-sync-log.txt
  exit
fi
