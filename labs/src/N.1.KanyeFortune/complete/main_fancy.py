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


def get_kanye_fortune()->str:
  """Hits a public API to get a random quotation from Kanye West

  Returns:
      str: Kanye Quote. Warning: he gets salty
  """
  with requests.get('http://api.kanye.rest') as response:
    return response.json()['quote']


def get_cat_fortune()->str:
  """Hits a public API to get a random cat fact

  Returns:
      str: Cat fact
  """
  with requests.get('https://cat-fact.herokuapp.com/facts/random') as response:
    return response.json()['text']


def main(get_fortune):
  message = get_fortune()
  print('\nYour fortune is:')
  print(f'   {message}\n\n')

if __name__ == "__main__":
    main(get_cat_fortune)
