"""

# Lab: Fizz Buzz - Blinky Edition

## Summary: 

Surprisingly, lots of professional programmers can't really 
code[1]. FizzBuzz is a classic interview question for sussing-out 
the non-skilled. 
                  
Here it is:
    Write a program that sequentially lights up an LED in a square grid.
    But--
      * For multiples of 3 color the LED red 
      * For the multiples of 5 color the LED green
      * For numbers which are multiples of both 3 and 5 color the LED blue

## Requirements
* Pause for .2 seconds before moving on to the next item
* Start over again at the beginning

Notes:
1. https://blog.codinghorror.com/why-cant-programmers-program/

Icons here: 
  - https://www.flaticon.com/packs/nature-134
  - https://www.flaticon.com/packs/weather-238
  - https://www.flaticon.com/packs/weather-141


"""
import os
import unicornhathd
import math
import requests
import time
from PIL import Image
from enum import Enum

this_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(this_directory)



class Forecast(Enum):
  Sun=1
  Snow=2
  Thunder=3
  Wind=4
  Storm=5


icons = {
  Forecast.Snow:'snow.png',
  Forecast.Sun:'sun.png',
  Forecast.Thunder: 'thunder.png',
  Forecast.Wind:'wind.png',
  Forecast.Storm:'storm.png'
}



def getImage(forecast):
  img_file = os.path.join(parent_directory, f'_data/{icons[forecast]}')
  return Image.open(img_file)


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



def draw():
  width=16
  height=16
  unicornhathd.set_rotation(-90)
  img = getImage(Forecast.Sun)

  try:
      while True:
        for x in range(width):
          for y in range(height):
                pixel = img.getpixel(( y, x))
                r, g, b, o = int(pixel[0]), int(pixel[1]), int(pixel[2]),float(pixel[3])
                if(o>0):
                  unicornhathd.set_pixel(x, y, r, g, b)

        unicornhathd.show()
        time.sleep(0.5)

  except KeyboardInterrupt:
      unicornhathd.off()


def main():
  draw()
  return
  geo_location = get_geo_location()
  grid_location = get_grid_location(geo_location["latitude"],geo_location["longitude"])
  forecast = get_forecast(grid_location["office"], grid_location["x"], grid_location["y"])
  
if __name__ == "__main__":
    main()

