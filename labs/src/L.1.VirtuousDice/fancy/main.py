"""


"""

import random
from enum import Enum
try: 
  from .dice import Die,Cup
except:
  pass


class Outcome(Enum):
  Undecided=0
  Win=1
  Loss=2


class Game:
  def __init__(self,playerName):
    self.playerName=playerName
    self.outcome = Outcome.Undecided
    self.cup= Cup()
  
  def shoot(self):
    self.cup.roll()
    print(f'{self.playerName} rolls a {self.cup.value}')
    return self.cup.value
  
  def finish_game(self,outcome:Outcome):
    self.outcome= outcome
    print(f'Game Over: {outcome.name} for {self.playerName}!')
  
  def do_first_roll(self):
    result = self.shoot()
    if result in [2,3,12]:
      self.finish_game(Outcome.Loss)
    if result in [7,11]:
      self.finish_game(Outcome.Win)
    self._first_roll=result

  def do_next_roll(self):
    result = self.shoot()
    if result==7:
      self.finish_game(Outcome.Loss)
    if result==self._first_roll:
      self.finish_game(Outcome.Win)

  def play(self):
    self.do_first_roll()
    while(self.outcome == Outcome.Undecided):
      self.do_next_roll()


class Table:
  def __init__(self,players):
    self.players = players
    self.gameNumber=0  

  def getCurrentPlayer(self):
    playerCount = len (self.players)
    return self.players[self.gameNumber%playerCount]

  def playGame(self):
    self.gameNumber += 1
    game = Game(self.getCurrentPlayer())
    game.play()
    print('\n')
  


def main():
  table = Table(["Lizzy", "Kim", "Alphonso", "Martin"])
  for i in range(10):
    table.playGame()


if __name__ == "__main__":
  from dice import Die,Cup
  main()

