import random
import os
from typing import List


def get_data_file() -> str:
    """Gets the absolute path of the file holding fortunes

    Returns:
        str: path
    """
    this_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(this_directory)
    return os.path.join(parent_directory, '_data/people')


def get_fortunes(data_file: str) -> List[str]:
    """Gets a list of strings from a data file

    Returns:
        List[str]: Fortunes
    """
    fortune_text = ''
    with open(data_file) as reader:
        fortune_text = reader.read()
    return [fortune.strip() for fortune in fortune_text.split('%')]


def get_fortune() -> str:
    """Gets a single fortune at random

    Returns:
        str: 1 fortune
    """
    data_file = get_data_file()
    fortunes = get_fortunes(data_file)
    return random.choice(fortunes)


def main():
    print('\nYour fortune is:')
    print(f'   {get_fortune()}\n\n')


if __name__ == "__main__":
    main()
