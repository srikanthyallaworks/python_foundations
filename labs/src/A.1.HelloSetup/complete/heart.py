import unicornhathd
import time, colorsys
import numpy

# Adapted from:
# https://learn.pimoroni.com/tutorial/tanya/be-still-my-beating-heart


unicornhathd.brightness(1)
unicornhathd.set_rotation(90)

heart = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0],
         [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
         [0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
         [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
         [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
         [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]  

heart = numpy.array(heart)


def numbers():
    yield from [11-n for n in range(1,11)]
    yield from range(1,10)
    yield from [11-n for n in range(1,11)]
    yield from range(1,10)

while True:
  for i in numbers():
    for y in range(16):
      for x in range(16):
        h = 0.0
        s = 1.0
        v = heart[x,y] / float(i)
        rgb = colorsys.hsv_to_rgb(h, s, v)
        r = int(rgb[0]*255.0)
        g = int(rgb[1]*255.0)
        b = int(rgb[2]*255.0)
        unicornhathd.set_pixel(x, y, r, g, b)
    unicornhathd.show()
    time.sleep(0.0005)
  time.sleep(0.8)