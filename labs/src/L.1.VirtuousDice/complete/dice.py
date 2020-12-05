

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
  _die_count=3

  def __init__(self):
    self._dice = [Die() for i in range(Cup._die_count)]

  def roll(self)->int:
    return sum([die.roll() for die in self._dice])

  @property
  def value(self)->int:
    return sum([die.value for die in self._dice])
