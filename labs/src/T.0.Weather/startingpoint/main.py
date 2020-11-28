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
  - https://www.flaticon.com/free-icon/sun_2698194?term=sunny&page=1&position=34

"""
import os
import unicornhathd
import math
import requests
import time
from PIL import Image

this_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(this_directory)
img_file = os.path.join(parent_directory, '_data/snow.png')
img = Image.open(img_file)


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

width=16
height=16

unicornhathd.set_rotation(-90)

def draw():
  try:
      while True:
          for o_x in range(int(img.size[0] / width)):
              for o_y in range(int(img.size[1] / height)):

                  valid = False
                  for x in range(width):
                      for y in range(height):
                          pixel = img.getpixel(((o_x * width) + y, (o_y * height) + x))
                          r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                          if r or g or b:
                              valid = True
                          unicornhathd.set_pixel(x, y, r, g, b)

                  if valid:
                      unicornhathd.show()
                      time.sleep(0.5)

  except KeyboardInterrupt:
      unicornhathd.off()


def main():
  draw()
  #print('\n\n\n===========================\n')
  #print(get_geo_location())
  #print(get_grid_location(39.7628,-105.0263))
  #print('\n\n\n\n')

if __name__ == "__main__":
    main()

