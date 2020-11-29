"""

https://realpython.com/api-integration-in-python/
https://en.wikipedia.org/wiki/Fortune_(Unix)


## Requirements
1. 

## Stretch Goals
1. Read-in the actual format.
2. Support command-line options

"""

import requests

def get_fortune():
  response = requests.get('http://api.kanye.rest')
  json = response.json()
  response.close()
  return json['quote']

def main():
  message = get_fortune()
  print('\nYour fortune is:')
  print(f'   {message}\n\n')

if __name__ == "__main__":
    main()