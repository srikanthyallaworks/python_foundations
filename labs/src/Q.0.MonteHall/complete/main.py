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
    message = 'Closed'
    if self.state==DoorState.InitialSelection:
      message += ' *'
    return message

class Game:
  def __init__(self):
    prizes = [
      Prize('car',100),
      Prize('goat',0),
      Prize('goat',0)
    ]
    random.shuffle(prizes)
    self._doors= [Door(prize) for prize in prizes]

  def __str__(self):
    msg=''
    for i,door in enumerate(self._doors):
      msg+=f'Door #{i+1}: {door}\n'
    return msg

  def reveal_goat(self):
    for d in self._doors:
      if d.state==DoorState.Closed:
        if d.prize.value==0:
          d.state=DoorState.Open
          return

  def select_initial(self,door_number):
    self._doors[door_number].state=DoorState.InitialSelection

  def select_final(self,door_number):
    return self._doors[door_number].prize



def play_interactive():
  game = Game()
  print(game)
  print('Pick a door [1,2,3]')
  initial_door_no = int(input('? '))
  game.select_initial(initial_door_no-1)

  print('\nNow, monty will reveal a goat:')
  game.reveal_goat()
  print(game)

  print('\nMake your final selection [1,2,3]')
  final_door_no = int(input('? '))
  prize = game.select_final(final_door_no-1)
  print(f"You've won a {prize.name} worth ${prize.value}!!")


def main():
  print("Let's play a game!")
  play_interactive()

if __name__ == '__main__':
  main()
