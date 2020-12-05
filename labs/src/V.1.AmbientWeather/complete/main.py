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
import time
from PIL import Image
from enum import Enum
try: from .forecast import get_local_forecast
except: pass

rows=16
columns=16
poll_frequency=90

class Forecast(Enum):
  Unknown=0
  Sun=1
  Snow=2
  Rain=3

icons = {
  Forecast.Snow:'snow.png',
  Forecast.Sun:'sun.png',
  Forecast.Rain: 'rain.png',
  Forecast.Unknown:'unknown.png',
}

def to_image(forecast):
  this_directory = os.path.dirname(__file__)
  parent_directory = os.path.dirname(this_directory)
  img_file = os.path.join(parent_directory, f'_assets/{icons[forecast]}')
  return Image.open(img_file)


def to_forecast(short_forecast):
  lowered = short_forecast.lower()
  if "sun" in lowered:
    return Forecast.Sun
  if "rain" in lowered:
    return Forecast.Rain
  if "snow" in lowered:
    return Forecast.Snow
  return Forecast.Unknown




def get_image():
  short_forecast = get_local_forecast()
  forecast = to_forecast(short_forecast)
  return to_image(forecast)


def update():
  img = get_image()

  for row in range(rows):
    for column in range(columns):
      pixel = img.getpixel(( column, row))
      r, g, b, o = int(pixel[0]), int(pixel[1]), int(pixel[2]),float(pixel[3])
      if(o>0):
        unicornhathd.set_pixel(row, column, r, g, b)

  unicornhathd.show()


def run():
  unicornhathd.set_rotation(90)
  while True:
    update()
    time.sleep(poll_frequency)


def main():
  try:
    run()
  except KeyboardInterrupt:
    unicornhathd.off()

  
if __name__ == "__main__":
  from forecast import get_local_forecast
  main()

