import unicornhathd
import time
import requests
try:
  from .settings import get_settings
  from .status import Status
except:
  from settings import get_settings
  from status import Status

settings= get_settings()

url = f'http://127.0.0.1:{settings.port}/status'

def to_color(status:Status):
  if status=='green':
    return (0, 128, 0)
  if status == 'yellow':
    return (255, 255, 0)
  if status == 'red':
    return (255,0,0)
  return (100,100,100)

def get_color():
  with requests.get(url) as response:
    message = response.json()
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
