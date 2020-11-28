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

import unicornhathd
import math
import random


rows,columns=16,16

def getPosition(n):
  return random.randrange(0,rows),random.randrange(0,columns)

def toColor(n):
  return (255,255,255)

def main():

  unicornhathd.brightness(1)
  unicornhathd.set_all(0,0,0)

  for i in range(rows*columns):
    row,column = getPosition(i)
    r,g,b = toColor(i)
    unicornhathd.set_pixel(row,column,r,g,b)
    unicornhathd.show()


if __name__ == "__main__":
    main()

