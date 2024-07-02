import urllib.request
import json

ip_api = "https://api.seeip.org/geoip"
wx_api_points = "https://api.weather.gov/points"

with urllib.request.urlopen(ip_api) as ip_geolocation_request:
    ip_geolocation_response = json.load(ip_geolocation_request)

# Geolocation variables
pub_ip = ip_geolocation_response['ip']
lat = ip_geolocation_response['latitude']
longitude = ip_geolocation_response['longitude']
city = ip_geolocation_response['city']
state = ip_geolocation_response['region']
country = ip_geolocation_response['country_code3']

print ("\n === IP Information ===")
print (f"IP address: {pub_ip}")
print (f"Location: {city}, {state}, {country}")
    

with urllib.request.urlopen(f"{wx_api_points}/{lat},{longitude}") as wx_request:
    wx_response = json.load(wx_request)

wx_response_string = json.dumps(wx_response, indent=4)
# print (wx_response_string)


with urllib.request.urlopen(f'{wx_response['properties']['forecast']}') as wx_forecast_request:
    wx_forecast_response = json.load(wx_forecast_request)

wx_forecast_response_string = json.dumps(wx_forecast_response, indent=4)
# print (wx_forecast_response_string)

temp = wx_forecast_response['properties']['periods'][0]['temperature']
temp_unit = wx_forecast_response['properties']['periods'][0]['temperatureUnit']

print ("\n === Weather ===")
print (f"Local temperature: {temp} {temp_unit}")
print (f'Today\'s Weather: {wx_forecast_response['properties']['periods'][0]['detailedForecast']}\n')