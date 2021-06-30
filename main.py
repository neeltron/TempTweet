import os
import requests

def fetch_weather_data(location):
  api_key = os.environ['weather_api']
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  city_name = location
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"] - 273.15
    return current_temperature
  else:
      print("Location out of reach")



city = input("Enter your City: ")
temperature = fetch_weather_data(city)
print(temperature)
