#!/bin/bash

####################################################################
# Script Name : wx.sh
# Description: Curls the weather from NOAA, dumps the information
#              into the command line or into a file for later entry
#              into a database.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

# TODO:
# This script could use so much refactoring to make it way cleaner.

# Define Location variables
HAMPTONWX=http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KLFI.TXT
CHARLESTONWX=http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KCHS.TXT
COLUMBIAWX=http://tgftp.nws.noaa.gov/data/observations/metar/decoded/KCUB.TXT

# Define Date variables
YEARDIR=`date +%Y`
MONTHDIR=`date +%B`
DAYDIR=`date +%d`
HOUR=`date +%H%M`

# Define Directories variables
WXDIR=/home/sparky/Documents/weather/
MKHAMPTONDIR=`mkdir -p $WXDIR/hampton/$YEARDIR/$MONTHDIR/$DAYDIR`
NEWHAMPTONDIR=$WXDIR/hampton/$YEARDIR/$MONTHDIR/$DAYDIR
MKCHARLESTONDIR=`mkdir -p $WXDIR/charleston/$YEARDIR/$MONTHDIR/$DAYDIR`
NEWCHARLESTONDIR=$WXDIR/charleston/$YEARDIR/$MONTHDIR/$DAYDIR
MKCOLUMBIADIR=`mkdir -p $WXDIR/columbia/$YEARDIR/$MONTHDIR/$DAYDIR`
NEWCOLUMBIADIR=$WXDIR/columbia/$YEARDIR/$MONTHDIR/$DAYDIR
HAMPTONTEMPDIR='mkdir -p /tmp/weather/hampton/'
CHARLESTONTEMPDIR='mkdir -p /tmp/weather/charleston'
COLUMBIATEMPDIR='mkdir -p /tmp/weather/columbia/'


function hampton_wx(){
curl -s $HAMPTONWX | sed -n '1p' | awk '{print $1,$2,$3,$4,$5,$6,$7,$8}'
curl -s $HAMPTONWX | sed -n '2p' | awk '{print $1,$2,$3,$4,$5,$6,$7}'
curl -s $HAMPTONWX | sed -n '3p' | awk '{print $1,$4,$7,$8,$9,"with",$14,$15,"gusts"}'
curl -s $HAMPTONWX | sed -n '4p' | awk '{print $1,$2,$3}' | sed -e 's/\:0\>//g'
curl -s $HAMPTONWX | sed -n '5p'
curl -s $HAMPTONWX | sed -n '6p' | awk '{print $1,$2,$3}'
curl -s $HAMPTONWX | sed -n '7p' | awk '{print $1,$2,$3,$4}'
curl -s $HAMPTONWX | sed -n '8p'
curl -s $HAMPTONWX | sed -n '9p' | awk '{print $1,$2,$3,$4}'
}

function charleston_wx(){
curl -s $CHARLESTONWX | sed -n '1p' | awk '{print $1,$2,$3,$4,$5,$6,$7}'
curl -s $CHARLESTONWX | sed -n '2p' | awk '{print $1,$2,$3,$4,$5,$6,$7}'
curl -s $CHARLESTONWX | sed -n '3p' | awk '{print $1,$4,$7,$8,$9,"with",$14,$15,"gusts"}'
curl -s $CHARLESTONWX | sed -n '4p' | awk '{print $1,$2,$3}' | sed -e 's/\:0\>//g'
curl -s $CHARLESTONWX | sed -n '5p'
curl -s $CHARLESTONWX | sed -n '6p' | awk '{print $1,$2,$3}'
curl -s $CHARLESTONWX | sed -n '7p' | awk '{print $1,$2,$3,$4}'
curl -s $CHARLESTONWX | sed -n '8p'
curl -s $CHARLESTONWX | sed -n '9p' | awk '{print $1,$2,$3,$4}'
}

function columbia_wx(){
curl -s $COLUMBIAWX | sed -n '1p' | awk '{print $1,$2,$3,$4,$5,$6,$7,$8}'
curl -s $COLUMBIAWX | sed -n '2p' | awk '{print $1,$2,$3,$4,$5,$6,$7}'
curl -s $COLUMBIAWX | sed -n '3p' | awk '{print $1,$4,$7,$8,$9,"with",$14,$15,"gusts"}'
curl -s $COLUMBIAWX | sed -n '4p' | awk '{print $1,$2,$3}' | sed -e 's/\:0\>//g'
curl -s $COLUMBIAWX | sed -n '5p'
curl -s $COLUMBIAWX | sed -n '6p' | awk '{print $1,$2,$3}'
curl -s $COLUMBIAWX | sed -n '7p' | awk '{print $1,$2,$3,$4}'
curl -s $COLUMBIAWX | sed -n '8p'
curl -s $COLUMBIAWX | sed -n '9p' | awk '{print $1,$2,$3,$4}'
}

$MKHAMPTONDIR
$HAMPTONTEMPDIR
$MKCHARLESTONDIR
$CHARLESTONTEMPDIR
$MKCOLUMBIADIR
$COLUMBIATEMPDIR

hampton_wx > /tmp/weather/hampton/new-weather-hampton
charleston_wx > /tmp/weather/charleston/new-weather-charleston
columbia_wx > /tmp/weather/columbia/new-weather-columbia

mv /tmp/weather/hampton/new-weather-hampton /tmp/weather/hampton/$HOUR
mv /tmp/weather/charleston/new-weather-charleston /tmp/weather/charleston/$HOUR
mv /tmp/weather/columbia/new-weather-columbia /tmp/weather/columbia/$HOUR

mv /tmp/weather/hampton/$HOUR $NEWHAMPTONDIR
mv /tmp/weather/charleston/$HOUR $NEWCHARLESTONDIR
mv /tmp/weather/columbia/$HOUR $NEWCOLUMBIADIR
