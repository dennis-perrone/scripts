#!/bin/bash

date=`date +%Y-%m-%d`
wikiPath="$HOME/development/wiki"
wikiDir=("public" "private")

for i in ${wikiDir[@]}; do
  cd $wikiPath/$i
  if [[ $(git status --porcelain=v1 2>/dev/null | wc -l) -ge 1 ]]; then
    cat index.md > README.md
    git add .
    git commit -am "Update wiki content for $date."
    git push
    echo "$(date +%Y-%m-%d\ \(%a\)): Successfully pushed $i wiki to GitHub." >> /home/$USER/cron-sync-log.txt
  else
    echo "$(date +%Y-%m-%d\ \(%a\)): No changes have been made to the $i repo since the last push to GitHub." >> /home/$USER/cron-sync-log.txt
  fi
done
