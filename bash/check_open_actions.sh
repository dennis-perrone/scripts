#!/bin/bash

wikiDir=$HOME/wiki
actionCount=$(grep -Rnw $wikiDir -e '\[ \]' --color=auto | wc -l)
#grep -Rnw $WIKI_DIR -e '\[ \]' --color=auto

if [[ $actionCount -ge 1 ]]; then
  grep -Rnw $wikiDir -e '\[ \]' --color=auto
else
 echo "All action items are accounted for!"
fi
