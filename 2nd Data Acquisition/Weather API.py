import requests
import json

apikey = "c48227c503c763a6ebebdf607999a5cd"

cities = ["Seoul,KR","Tokyo,JP","New York,US"]
cities_US = ["San Francisco,US","Los Angeles,US","Las Vegas,US"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
k2c = lambda k: k-273.15

def group1(): 
  for name in cities:

    url = api.format(city_name=name, api_key= apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print("+ CITY =", data["name"])
    print("| WEATHER =", data["weather"][0]["description"])
    print("| MIN TEMP =",k2c(data["main"]["temp_min"]))
    print("| MAX TEMP =",k2c(data["main"]["temp_max"]))
    print("| HUMIDITY =",data["main"]["humidity"])
    print("| PRESSURE =",data["main"]["pressure"])
    print("| DEG =",data["wind"]["deg"])
    print("| SPEED =",data["wind"]["speed"])
    print("")  

def group2(): 
  for name in cities_US:

    url = api.format(city_name=name, api_key= apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print("+ CITY =", data["name"])
    print("| CLOUDS =",data["clouds"]["all"])
    print("| WEATHER =", data["weather"][0]["description"])
    print("| FELLS LIKE =",format(k2c(data["main"]["feels_like"]),".2f"))
    print("| MIN TEMP =",format(k2c(data["main"]["temp_min"]),".2f"))
    print("| MAX TEMP =",format(k2c(data["main"]["temp_max"]),".2f"))
    print("| HUMIDITY =",data["main"]["humidity"])
    print("")  


group1()
group2()
