#!/bin/bash

# Validates that there is an argument passed to the script.
if [[ -z $1 ]]; then
  echo "Script usage: $0 \"company_role_title\""
  echo "Exiting script ..."
  exit
fi

role_string=$(echo "$1" | tr '[:upper:]' '[:lower:]')
role_title="${role_string// /_}"
new_role=$HOME/wiki/private/career/$role_title.md

if [[ ! -f $new_role ]]; then
  echo "# $1"> $new_role
  #echo "# $role_string"> $new_role
  echo "" >> $new_role
  echo "## Position Information" >> $new_role
  echo "" >> $new_role
  echo "- Date Posted: $(date +%Y-%m-%d)" >> $new_role
  echo "- Date Applied: $(date +%Y-%m-%d)" >> $new_role
  echo "- Referred [Y/N]:" >> $new_role
  echo "- Position ID:" >> $new_role
  echo "- Link to job: [here]()" >> $new_role
  echo "- Salary:" >> $new_role
  echo "- Travel:" >> $new_role
  echo "- Clearance Required:" >> $new_role
  echo "" >> $new_role
  echo "## Job Overview" >> $new_role
  echo "" >> $new_role
  echo "- " >> $new_role
  echo "" >> $new_role
  echo "## Required Skills" >> $new_role
  echo "" >> $new_role
  echo "- " >> $new_role
  echo "" >> $new_role
  echo "## Preferred Skills" >> $new_role
  echo "" >> $new_role
  echo "## Notes" >> $new_role
  echo "" >> $new_role
  echo "- $(date +%Y-%m-%d): " >> $new_role
else
  echo "$new_role already exists ..."
fi

echo "- [$1](/career/$role_title.md)" >> ~/wiki/private/career/index.md

nvim -c "norm Go" $new_role
