#!/bin/bash

# Validates that there is an argument passed to the script.
if [[ -z $2 ]]; then
  echo "Script usage: $0 \"class number\" \"class description\""
  echo "Exiting script ..."
  exit
fi

read -p "Enter the class start date (YYYY-MM-DD): " class_start
#read -p "Enter the class name (ex. IT625): " class_lower

class_lower=$(echo "$1" | tr '[:upper:]' '[:lower:]')
class_upper=$(echo "$1" | tr '[:lower:]' '[:upper:]')
class_dir=$HOME/wiki/private/college
weeks=10

if [[ ! -f $class_dir/index_$class_lower.md ]]; then
  echo "# $class_upper: $2" >> $class_dir/index_$class_lower.md
  echo "" >> $class_dir/index_$class_lower.md
  echo "## Class Information" >> $class_dir/index_$class_lower.md
  echo "" >> $class_dir/index_$class_lower.md
  echo "- Start Date: $class_start" >> $class_dir/index_$class_lower.md
  echo "- End Date: $(date +%Y-%m-%d -d "$class_start + $weeks week - 1 day")" >> $class_dir/index_$class_lower.md
  echo "- Professor:" >> $class_dir/index_$class_lower.md
  echo "" >> $class_dir/index_$class_lower.md
  echo "## Course Notes" >> $class_dir/index_$class_lower.md
  echo "" >> $class_dir/index_$class_lower.md
  for i in $(seq -w 1 $weeks); do
    echo "- [Module $i](/college/$class_lower/$class_lower"_module_$i.md")" >> $class_dir/index_$class_lower.md
  done
  echo "" >> $class_dir/index_$class_lower.md
  echo "## Resources" >> $class_dir/index_$class_lower.md
  echo "" >> $class_dir/index_$class_lower.md
  echo "1. [Placeholder](placeholder)" >> $class_dir/index_$class_lower.md
  echo "The class index for $class_upper has been created."
else
  echo "The class index for $class_upper has already been created."
fi

if [[ ! -d $class_dir/$class_lower ]]; then
  mkdir -p $class_dir/$class_lower
  for i in $(seq -w 1 $weeks); do
    week_start=$(date +%Y-%m-%d -d "$class_start + $i week - 1 week")
    week_end=$(date +%Y-%m-%d -d "$week_start + 6 day")

    echo "# $class_upper Module $i" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "## Module Information" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "- Week $i Start: $week_start" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "- Week $i End: $week_end" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    #echo "- Start Date: $week_start" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    #echo "- End Date: $week_end" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "## Notes" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "### Source" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "- " >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "## References" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
    echo "1. [Placeholder](placeholder)" >> $class_dir/$class_lower/$class_lower'_module_'$i.md
  done
  echo "The class directory for $class_upper ($2) has been created."
else
  echo "The class directory for $class_upper ($2) has already been created."
fi
