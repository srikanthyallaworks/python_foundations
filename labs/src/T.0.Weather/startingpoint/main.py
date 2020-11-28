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

"""

import unicornhathd
import math
import requests
import time
from PIL import Image


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
  json = fetch(url)["properties"]
  return {}

def main():
  print('\n\n\n===========================\n')
  #print(get_geo_location())
  print(get_grid_location(39.7628,-105.0263))
  print('\n\n\n\n')

if __name__ == "__main__":
    main()

