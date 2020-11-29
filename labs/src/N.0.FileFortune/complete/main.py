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

def get_fortunes():
  fortunes = []
  reader = open(data_file)
  for line in reader:
    fortunes.append(line)
  reader.close()
  return fortunes

def main():
  fortunes=get_fortunes()
  message = random.choice(fortunes)
  print('\nYour fortune is:')
  print(f'   {message}\n\n')

if __name__ == "__main__":
    main()
