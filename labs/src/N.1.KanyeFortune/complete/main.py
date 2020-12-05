import requests

def get_kanye_fortune()->str:
  """Hits a public API to get a random quotation from Kanye West

  Returns:
      str: Kanye Quote. Warning: he gets salty
  """
  response = requests.get('http://api.kanye.rest')
  json = response.json()
  response.close()
  return json['quote']


def get_cat_fortune()->str:
  """Hits a public API to get a random cat fact

  Returns:
      str: Cat fact
  """
  response = requests.get('https://cat-fact.herokuapp.com/facts/random')
  json = response.json()
  response.close()
  return json['text']

get_fortune = get_cat_fortune

def main():
  message = get_fortune()
  print('\nYour fortune is:')
  print(f'   {message}\n\n')

if __name__ == "__main__":
    main()
