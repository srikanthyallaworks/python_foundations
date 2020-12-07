from dataclasses import dataclass
from enum import Enum
import random
from typing import Tuple


def first(predicate, iterable):
  for item in iterable:
    if predicate(item):
      return item

@dataclass(frozen=True)
class Prize:
  name:str 
  value:int

@dataclass(frozen=True)
class Prizes:
  def build_goat():
    return Prize('goat',0)
  def build_car():
    return Prize('car',100)   


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
      Prizes.build_car(),
      Prizes.build_goat(),
      Prizes.build_goat()
    ]
    random.shuffle(prizes)
    return [Door(prize) for prize in prizes]


def choose_stick(doors):
  def is_stick_door(door:Door):
    return door.state==DoorState.InitialSelection
  return first(is_stick_door,doors)

def choose_swap(doors):
  def is_swap_door(door:Door):
    return door.state==DoorState.Closed
  return first(is_swap_door,doors)


def pick_door_to_reveal(doors):
  def is_candidate(door:Door):
    return door.state!=DoorState.InitialSelection and door.prize.value==0
  return first(is_candidate,doors)


def play(chooser)->int:
  doors = Doors.build_random()

  selection = random.choice(doors)
  selection.state=DoorState.InitialSelection

  revealed_goat = pick_door_to_reveal(doors)
  revealed_goat.state=DoorState.Open

  final_selection = chooser(doors)
  print(f'Won a {final_selection.prize.name}!')
  return final_selection.prize.value


total_winnings=0
games_to_play=100


for i in range(games_to_play):
  
  total_winnings += play(choose_stick)

print(f'\n\nPer-game winnings: {total_winnings/games_to_play}')

