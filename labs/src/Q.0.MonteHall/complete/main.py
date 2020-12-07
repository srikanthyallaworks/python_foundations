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




@dataclass
class Host:
  name:str
  def reveal_goat(self,doors)->Door:
    def is_candidate(door:Door):
      return door.state!=DoorState.InitialSelection and door.prize.value==0
    return first(is_candidate,doors)



class Contestant:
  def __init__(self,name):
    self.name=name

  def make_initial_selection(self,doors):
    return random.choice(doors)

  def is_stick_door(door:Door):
    return door.state==DoorState.InitialSelection

  def is_swap_door(door:Door):
    return door.state==DoorState.Closed

  def make_final_selection(self,doors)->Door:
    raise Exception('Not implemented')

class Swapper(Contestant):
  def make_final_selection(self,doors)->Door:
    return first(Contestant.is_swap_door,doors)

class Sticker(Contestant):
  def make_final_selection(self,doors)->Door:
    return first(Contestant.is_stick_door,doors)



class SwappingContestant(Contestant):
  

  def make_final_selection(self,doors)->Door:
    def stick(door:Door):
      return door.state==DoorState.InitialSelection
    def swap(door:Door):
      return door.state==DoorState.Closed
    return first(stick,doors)


@dataclass
class Game:
  host:Host
  contestant:Contestant
  doors:Tuple[Door,Door,Door]

  def play(self)->int:
    selection = self.contestant.make_initial_selection(self.doors)
    selection.state=DoorState.InitialSelection

    revealed_goat = self.host.reveal_goat(self.doors)
    revealed_goat.state=DoorState.Open

    final_selection = self.contestant.make_final_selection(self.doors)
    print(f'Won a {final_selection.prize.name}!')
    return final_selection.prize.value


total_winnings=0
games_to_play=100

host = Host('Monte')
contestant = Sticker('Joe')

for i in range(games_to_play):
  doors = Doors.build_random()
  game = Game(host,contestant,doors)
  total_winnings += game.play()

print(f'\n\nPer-game winnings: {total_winnings/games_to_play}')

