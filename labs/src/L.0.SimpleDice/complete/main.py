

import random


class Die:

  def __init__(self,side_count=6):
    """Sets up the class

    Args:
        side_count (int): Number of sides.
    """
    self._side_count=side_count

  
  def roll(self):
    """Rolls the die

    Returns:
        int: Some random value from 1 up to the number of sides 
    """
    return random.randrange(1,self._side_count+1)


class Cup:
  def __init__(self,dice):
    """Sets up the cup

    Args:
        dice (list[Die]): Dice to put in the cup
    """
    self._dice = dice


  def roll(self):
    """Rolls all dice in the cup

    Returns:
        int: sum of the dice rolls
    """
    total=0
    for die in self._dice:
      total+=die.roll()
    return total



def main():
  dice = (Die(6), Die(6),Die(12))
  cup = Cup(dice)
  result = cup.roll()
  while result != 18:
    print(f'Rolled a {result}')
    result = cup.roll()
  print("18! You won!")


if __name__ == "__main__":
    main()
