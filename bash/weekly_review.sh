#!/bin/bash

weekly_review=$HOME/wiki/private/weekly-reviews/week_$(date +%W)_review.md

if [[ ! -f $weekly_review ]]; then
  echo "# Weekly Review for Week $(date +%W)" >> $weekly_review
  echo "" >> $weekly_review
  echo "Completed on: $(date +%Y-%m-%d)" >> $weekly_review
  echo "" >> $weekly_review
  echo "## Before the review" >> $weekly_review
  echo "" >> $weekly_review
  echo "- [ ] Process digital inboxes: " >> $weekly_review
  echo "  - [ ] Email" >> $weekly_review
  echo "  - [ ] LinkedIn" >> $weekly_review
  echo "  - [ ] Slack / Signal / Texts" >> $weekly_review
  echo "- [ ] Process physical inbox" >> $weekly_review
  echo "- [ ] Clean off desk" >> $weekly_review
  echo "- [ ] Put phone and computer on \"o Not Disturb mode\"" >> $weekly_review
  echo "" >> $weekly_review
  echo "## The weekly review" >> $weekly_review
  echo "" >> $weekly_review
  echo "- [ ] Review my Next Actions list" >> $weekly_review
  echo "- [ ] Review my Projects list" >> $weekly_review
  echo "- [ ] Review past and upcoming Calendar items" >> $weekly_review
  echo "- [ ] Review my Waiting For list" >> $weekly_review
  echo "" >> $weekly_review
  echo "## After the review" >> $weekly_review
  echo "" >> $weekly_review
  echo "- [ ] Reflect on the past week:" >> $weekly_review
  echo "  - [ ] What worked well" >> $weekly_review
  echo "  - [ ] What didn't work well" >> $weekly_review
  echo "  - [ ] What should I start doing" >> $weekly_review
  echo "- [ ] Review my Someday / Maybe list" >> $weekly_review
  echo "- [ ] Review any other relevant checklists" >> $weekly_review
else
  echo "$weekly_review already exists ..."
fi

echo "- [Week $(date +%W) Review](/weekly-reviews/week_$(date +%W)_review.md)" >> ~/wiki/private/weekly-reviews/index.md

nvim -c "norm gg" $weekly_review
