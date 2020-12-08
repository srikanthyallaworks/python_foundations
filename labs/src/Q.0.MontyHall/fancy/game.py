from dataclasses import dataclass
from enum import Enum
import random

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
  def __str__(self):
    if self.state==DoorState.Open:
      return self.prize.name
    if self.state==DoorState.InitialSelection:
      return '🚪 *'
    return '🚪'

class GameState(Enum):
  NeedInitialSelection=0
  NeedFinalSelection=1
  Complete=2

class Game:
  def __init__(self):
    self._state = GameState.NeedInitialSelection
    prizes = [
      Prize('🚗',100),
      Prize('🐐',0),
      Prize('🐐',0)
    ]
    random.shuffle(prizes)
    self._doors= [Door(prize) for prize in prizes]

  def __str__(self):
    msg=''
    for i,door in enumerate(self._doors):
      msg+=f'Door #{i+1}: {door}\n'
    return msg

  @property
  def doors(self):
      return self._doors

  def _reveal_goat(self):
    for d in self._doors:
      if d.state==DoorState.Closed:
        if d.prize.value==0:
          d.state=DoorState.Open
          return

  def select_initial(self,door_number):
    if self._state!=GameState.NeedInitialSelection:
      raise Exception("Already made an initial selection.")
    self._doors[door_number].state=DoorState.InitialSelection
    self._reveal_goat()
    self._state= GameState.NeedFinalSelection

  def select_final(self,door_number):
    if self._state!= GameState.NeedFinalSelection:
      raise Exception("Wrong state!")
    self.prize = self._doors[door_number].prize
    self._state=GameState.Complete
    return self.prize


