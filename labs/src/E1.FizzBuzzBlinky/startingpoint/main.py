"""



"""

import unicornhathd
import time
import math
import itertools

unicornhathd.brightness(1)
unicornhathd.set_all(0,0,255)

def getPosition(n):
  return (n%16, math.floor(n/16)%16)


def toColor(n):
    divisibleBy3 = n % 3 == 0
    divisibleBy5 = n % 5 == 0
    if divisibleBy3 and divisibleBy5:
        return (255,0,0)
    if divisibleBy3:
        return (0,255,0)
    if divisibleBy5:
        return (0,0,255)
    return (255,255,255)

def main():
  for i in itertools.count():
    row,column = getPosition(i)
    r,g,b = toColor(i)
    unicornhathd.set_all(0,0,0)
    unicornhathd.set_pixel(row,column,r,g,b)
    unicornhathd.show()
    time.sleep(.20)


if __name__ == "__main__":
    main()

