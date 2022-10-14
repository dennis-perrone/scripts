#!/usr/bin/python

####################################################################
# Script Name : main.py
# Description : Interface with the NOAA API
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import json
from pydoc import resolve
import requests
import config

points = config.points
office = config.noaa_office
grid_x = config.grid_x
grid_y = config.grid_y

# curl https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/hourly
# curl https://api.weather.gov/points/{points}


response = requests.get(f"https://api.weather.gov/points/{points}")
#response = requests.get(f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/hourly")

print (response.json())

# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text) 
    
# #jprint(response.json())

# daily_high = response.json()['properties']
# jprint(daily_high)