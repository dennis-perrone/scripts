#!/bin/bash

####################################################################
# Script Name : docked.sh
# Description : Script to switch to singlehead when undocked and not
#               running a desktop environment
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off --output DP-1-1 --off --output DP-1-2 --off --output DP-1-3 --off
