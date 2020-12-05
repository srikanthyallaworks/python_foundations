import os
import unicornhathd
import time
from PIL import Image
from enum import Enum
try: 
  from .forecast import get_local_forecast
except: 
  from forecast import get_local_forecast

rows,columns = unicornhathd.get_shape()

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
  main()

