
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

def get_fortunes(data_file):
  """Gets a list of strings from a data file

  Returns:
      List[str]: Fortunes
  """
  fortunes = []
  for line in open(data_file):
    fortunes.append(line)
  return fortunes

def get_fortune():
  """Gets a single fortune at random 

  Returns:
      str: 1 fortune
  """
  data_file = get_data_file()
  fortunes=get_fortunes(data_file)
  return random.choice(fortunes)


def main():
  print('\nYour fortune is:')
  print(f'   {get_fortune()}\n\n')


if __name__ == "__main__":
    main()
