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

from unicornhathd import unicornhathd
import time
import math
import itertools

rows,columns=16,16

def getPosition(n):
  return (n%rows, math.floor(n/columns)%columns)

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

  #unicornhathd.brightness(1)
  unicornhathd.set_all(0,0,255)

  for i in itertools.count():
    row,column = getPosition(i)
    r,g,b = toColor(i)
    unicornhathd.set_all(0,0,0)
    unicornhathd.set_pixel(row,column,r,g,b)
    unicornhathd.show()
    time.sleep(.20)

if __name__ == "__main__":
    main()
