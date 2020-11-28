#!/bin/bash

####################################################################
# Script Name : taskwarrior-review
# Description : Queries taskwarrior for tasks that have next
#               actions
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

echo 'Finding most urgent tasks in each project...'

# UUIDS is a string that will contain the UUID of every task we wish to see.
UUIDS=

# Enumerate pending task UUIDs having no project.
for uuid in $(task status='pending' and project='' _uuids)
do
  UUIDS="$UUIDS $uuid"
done

# Enumerate the project names for all active projects.
for project in $(task rc.list.all.projects=0 _projects)
do
  # Temporarily override the 'next' report output to yield only UUID, and only
  # one task.
  uuid=$(task project="$project" rc.verbose=nothing rc.report.next.columns=uuid rc.report.next.labels=uuid limit:1 next)
  UUIDS="$UUIDS $uuid"
done

# Run the next report, showing only the specific list of tasks.
task $UUIDS next
