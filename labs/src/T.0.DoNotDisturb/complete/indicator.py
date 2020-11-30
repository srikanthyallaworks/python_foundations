"""



"""

import unicornhathd
import time
import requests


red = (255,0,0)
yellow = (255, 255, 0)
green = (0, 128, 0)
unknown = (100,100,100)
url = 'http://127.0.0.1:5000/status'

def to_color(status):
  if status=='green':
    return green
  if status == 'yellow':
    return yellow
  if status == 'red':
    return red
  return unknown

def get_color():
  response = requests.get(url)
  message = response.json()
  response.close()
  return to_color(message['status'])

def run():
  unicornhathd.brightness(1)
  while True:
    r,g,b = get_color()
    unicornhathd.set_all(r,g,b)
    unicornhathd.show()
    time.sleep(5)

def main():
  try:
    run()
  except KeyboardInterrupt:
      unicornhathd.off()
  
if __name__ == '__main__':
  main()
