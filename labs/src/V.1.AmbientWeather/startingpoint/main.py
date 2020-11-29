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
from forecast import get_local_forecast



class Forecast(Enum):
  Sun=1
  Snow=2
  Thunder=3
  Wind=4
  Storm=5

class TimeOfDay(Enum):
  Day=100
  Night=101

icons = {
  Forecast.Snow:'snow.png',
  Forecast.Sun:'sun.png',
  Forecast.Thunder: 'thunder.png',
  Forecast.Wind:'wind.png',
  Forecast.Storm:'storm.png',
  TimeOfDay.Night:'night.png',
}

def getImage(forecast):
  this_directory = os.path.dirname(__file__)
  parent_directory = os.path.dirname(this_directory)
  img_file = os.path.join(parent_directory, f'_assets/{icons[forecast]}')
  return Image.open(img_file)


def get_short_forecast():
  return get_local_forecast()["properties"]["periods"][0]["shortForecast"]


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


  
if __name__ == "__main__":
    main()

