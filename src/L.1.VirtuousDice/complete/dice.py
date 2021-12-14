

import random


class Die:
  _side_count = 6

  def __init__(self):
    self._value = None

  def roll(self)->int:
    self._value = random.randrange(1,Die._side_count+1)
    return self._value

  @property
  def value(self)->int:
    return self._value


class Cup:

  def __init__(self,die_count=2):
    self._dice = [Die() for i in range(die_count)]

  def roll(self)->int:
    return sum([die.roll() for die in self._dice])

  @property
  def value(self)->int:
    return sum([die.value for die in self._dice])
