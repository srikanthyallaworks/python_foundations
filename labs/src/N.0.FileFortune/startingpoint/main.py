import random
import os

def get_data_file():
  """Gets the absolute path of the file holding fortunes

  Returns:
      str: path
  """
  this_directory = os.path.dirname(__file__)
  parent_directory = os.path.dirname(this_directory)
  return os.path.join(parent_directory, '_data/fortunes.txt')


def get_fortunes():
  """Gets a list of strings

  Returns:
      List[str]: Fortunes
  """
  return  [
    'TODO: Get fortunes from somewhere',
    'TODO: Choose one at random.',
  ]


def get_fortune():
  """Gets a single fortune 

  Returns:
      str: 1 fortune
  """
  fortunes = get_fortunes()
  return fortunes[0]


def main():
  print('\nYour fortune is:')
  print(f'   {get_fortune()}\n\n')




if __name__ == "__main__":
    main()
