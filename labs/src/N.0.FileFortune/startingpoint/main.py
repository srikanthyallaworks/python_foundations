"""

https://realpython.com/api-integration-in-python/
https://en.wikipedia.org/wiki/Fortune_(Unix)


## Requirements
1. 

## Stretch Goals
1. Read-in the actual format.
2. Support command-line options

"""
import random
import os

this_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(this_directory)
data_file = os.path.join(parent_directory, '_data/fortunes.txt')

fortunes = [
    'You will obey or molten silver will be poured into your ears.',
    'You will outgrow your usefulness.',
    'You will overcome the attacks of jealous associates.',
    'You will pass away very quickly.',
    'You will pay for your sins.  If you have already paid, please disregard this message.',
    'You will pioneer the first Martian colony.']

def get_fortune():
  return fortunes[0]

def main():
  message = get_fortune()
  print('\nYour fortune is:')
  print(f'   {message}\n\n')

if __name__ == "__main__":
    main()
