"""



"""

import random

class Die():

  def __init__(self,sideCount):
    self.sideCount=sideCount
    self._value = None

  def get_value(self):
    return self._value; 

  def roll(self) ->int:
    self._value = random.randrange(1,self.sideCount+1)
    return self._value


class Cup():

  def __init__(self,dice):
    self._dice = dice

  def roll(self)->int:
    total=0
    for die in self._dice:
      total+=die.roll()
    return total

  def get_value(self)->int:
    total=0
    for die in self._dice:
      total+=die.get_value()
    return total


def main():
  cup = Cup([Die(6),Die(6),Die(6)])
  while True:
    result = cup.roll()
    print(f'Rolled a {result}')
    if result==18:
      print('You won!')
      return  

if __name__ == "__main__":
    main()
