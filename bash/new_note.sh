#!/bin/bash

# Validates that there is an argument passed to the script.
if [[ -z $1 ]]; then
  echo "Script usage: $0 \"note topic\""
  echo "Exiting script ..."
  exit
fi

note_string=$(echo "$1" | tr '[:upper:]' '[:lower:]')
note_topic="${note_string// /_}"
new_note=$HOME/wiki/public/$note_topic.md

new_date () {
  date "+%Y-%m-%d %H:%M:%S %Z"
}

create_note () {
  echo "# $1"> $new_note
  echo "" >> $new_note
  echo "- Created:  $(new_date)" >> $new_note
  echo "- Modified: $(new_date)" >> $new_note
  echo "" >> $new_note
  echo "## Notes" >> $new_note
  echo "" >> $new_note
}

append_note () {
  sed -i "/- Modified: /c\- Modified: $(new_date)" $new_note
}

if [[ ! -f $new_note ]]; then
  create_note "$1"
  echo "- [$1]($note_topic.md)" >> ~/wiki/public/index.md
else
  echo "$new_note already exists ..."
  append_note
fi

nvim -c "norm Go-" $new_note
