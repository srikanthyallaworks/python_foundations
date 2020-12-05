"""



"""

import random

class Die:
  _side_count = 6

  def __init__(self):
    self._value = None

  def roll(self):
    self._value = random.randrange(1,Die._side_count+1)
    return self._value


class Cup:
  _die_count=3

  def __init__(self):
    self._dice = [Die() for i in range(Cup._die_count)]

  def roll(self):
    total=0
    for die in self._dice:
      total+=die.roll()
    return total


def main():
  cup = Cup()
  result = cup.roll()

  while result != 18:
    print(f'Rolled a {result}')
    result = cup.roll()

  print("18! You won!")


if __name__ == "__main__":
    main()
