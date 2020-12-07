# Lab: Fizz Buzz - Blinky Edition

## Summary 

Same as before, the idea here is to iterate through 
a sequence of numbers. But this time it's going to be 
graphical, lighting up LEDs on an SBC-- or at least 
a simulation of one.

## Hardware 
* 256 LEDs arranged in a square (16 rows, 16 columns)
* Each LED can be any color in the RGB spectrum
* Interface using Pimoroni's UnicornHatHD [interface](https://github.com/pimoroni/unicorn-hat-hd)

## Requirements   
1. Lights up each LED sequentially
2. Keep it lit for half a second
3. Only 1 LED is lit up at a time
4. Colors as follows
  * Multiples of 3: Red 
  * Multiples of 5: Green
  * Multiples of 3 and 5: Blue
  * Everything else: White
5. After the last LED, start over at the beginning


## Stretch Goals
* Write unit tests to document and test.
* Deploy to actual hardware.
















## Hints
* Check out the built-in function [range](https://docs.python.org/3/library/functions.html#func-range).
* To check divisibility, look into the operator [modulo](https://realpython.com/python-modulo-operator/)
* For unit tests, here's a reference on the built-in framework [unittest](https://docs.python.org/3/library/unittest.html)


