from dataclasses import dataclass
from enum import Enum
import random
from typing import Tuple, Iterable,Callable


def first(predicate, iterable):
  """find the first item matched by the predicate

  Args:
      predicate (Callable[[T],bool]): matches an item
      iterable (Sequence[T]): Sequence

  Raises:
      Exception: Throws if nothing is found

  Returns:
      [type]: The matched item from the sequence
  """

  for item in iterable:
    if predicate(item):
      return item
  raise Exception('Nothing found')


@dataclass(frozen=True)
class Prize:
  name:str 
  value:int

class DoorState(Enum):
  Closed=0
  InitialSelection=1
  Open=2


@dataclass
class Door:
  prize:Prize 
  state=DoorState.Closed


class Doors:
  def build_random():
    prizes = [
      Prize('car',100),
      Prize('goat',0),
      Prize('goat',0)
    ]
    random.shuffle(prizes)
    return [Door(prize) for prize in prizes]


def get_strategies(): 
  """Gets a map of name: callable
  """

  def sticker(doors):
    def is_stick_door(door:Door):
      return door.state==DoorState.InitialSelection
    return first(is_stick_door,doors)

  def swapper(doors):
    def is_swap_door(door:Door):
      return door.state==DoorState.Closed
    return first(is_swap_door,doors)

  def randomr(doors):
    closed_doors = [d for d in doors if d.state != DoorState.Open]
    return random.choice(closed_doors)

  strategies = [
    sticker,
    randomr,
    swapper
  ]
  return {s.__name__:s for s in strategies}
    


class Game:

  def pick_door_to_reveal(doors):
    def is_candidate(door:Door):
      return door.state!=DoorState.InitialSelection and door.prize.value==0
    return first(is_candidate,doors)


  def play(chooser)->int:
    doors = Doors.build_random()

    selection = random.choice(doors)
    selection.state=DoorState.InitialSelection

    revealed_goat = Game.pick_door_to_reveal(doors)
    revealed_goat.state=DoorState.Open

    final_selection = chooser(doors)
    return final_selection.prize.value





def test_strategies(game_count=100):
  strategies=get_strategies()
  winnings={k:0 for k in strategies}

  for i in range(game_count):
    for k in strategies:
      winnings[k]+=Game.play(strategies[k])

  return winnings




def main():
  results = test_strategies()
  print('\nResults:')
  for n,v in results.items():
    print(f'\t{n}:${v}')


if __name__ == '__main__':
  main()

