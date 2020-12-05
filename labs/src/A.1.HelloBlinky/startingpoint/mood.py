import unicornhathd
import colorsys
import random
import time


unicornhathd.brightness(1)
unicornhathd.set_all(0,0,255)

def pin(val):
  return max(0,min(val,1))

def nudge(val,factor):
  nudged= val + random.gauss(0,factor)
  return pin(nudged)

column = random.randrange(16)
row = random.randrange(16)
(r,g,b)=unicornhathd.get_pixel(row,column)
(h,s,v) = colorsys.rgb_to_hsv(r/255,g/255,b/255)

while True:
  column = (column + random.randrange(-1,2))%16
  row = (row + random.randrange(-1,2))%16
  h = nudge(h,.005)
  s = max(.85, nudge(s,.005))
  v = max(.85,nudge(v,.01))
  unicornhathd.set_pixel_hsv(row,column,h,s,v)
  if random.random()>.9:
    unicornhathd.show()
    time.sleep(.1)

