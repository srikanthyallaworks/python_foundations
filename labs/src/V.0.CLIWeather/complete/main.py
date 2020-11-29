"""

# Lab: Fizz Buzz - Blinky Edition



"""

import requests


def fetch(uri):
  response = requests.get(uri)
  if response.status_code != 200:
    raise ConnectionError("Couldn't Connect")
  json = response.json()
  response.close()
  return json


def get_geo_location():
  json = fetch('http://www.geoplugin.net/json.gp')
  return {
    "latitude": float(json["geoplugin_latitude"]),
    "longitude":float(json["geoplugin_longitude"])
  }


def get_grid_location(latitude, longitude):
  url = f'https://api.weather.gov/points/{latitude},{longitude}'
  json = fetch(url)["properties"]
  return {
    "office":json["cwa"],
    "x":int(json["gridX"]),
    "y":int(json["gridY"])
  }


def get_forecast(office,x,y):
  url = f'https://api.weather.gov/gridpoints/{office}/{x},{y}/forecast'
  return fetch(url)["properties"]["periods"][0]["shortForecast"]


def main():
  geo_location = get_geo_location()
  grid_location = get_grid_location(geo_location["latitude"],geo_location["longitude"])
  forecast = get_forecast(grid_location["office"], grid_location["x"], grid_location["y"])
  print(f'\n\nForecast:\n     {forecast}\n\n')
  
if __name__ == "__main__":
    main()

