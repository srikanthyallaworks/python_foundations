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

timeout_in_secords = 5


def get_kanye_fortune() -> str:
    """Hits a public API to get a random quotation from Kanye West

    Returns:
        str: Kanye Quote. Warning: he gets salty
    """
    with requests.get('http://api.kanye.rest', timeout=timeout_in_secords) as response:
        return response.json()['quote']


def get_cat_fortune() -> str:
    """Hits a public API to get a random cat fact

    Returns:
        str: Cat fact
    """
    with requests.get('https://cat-fact.herokuapp.com/facts/random', timeout=timeout_in_secords) as response:
        return response.json()['text']


def get_fortune():
    try:
        return get_cat_fortune()
    except:
        # TODO: Log this or something
        return "The future is cloudy"


def main():
    print('\nYour fortune is:')
    print(f'   {get_fortune()}\n\n')


if __name__ == "__main__":
    main()
