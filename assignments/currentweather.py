# currentweather.py
# current weather in Kyiv
# latitude 50.4547 longitude 30.5238
# author: Nataliia Dragunova

# current temperature in Kyiv(Ukraine)
'''
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=50.4547&longitude=30.5238&current=temperature_2m"
response = requests.get(url)
# print (response.json())
data = response.json()
# with open ("v1dump.json") as fp:
# json.dump(data)

current = data["current"]
temp = current["temperature_2m"]
# print(temp)
print(temp)
'''
# current wind direction (10m) in Kyiv(Ukraine)
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=50.4547&longitude=30.5238&current=wind_direction_10m"
response = requests.get(url)
# print (response.json())
data = response.json()
# with open ("v1dump.json") as fp:
# json.dump(data)

current = data["current"]
wind = current["wind_direction_10m"]
# print(wind)
print(wind)