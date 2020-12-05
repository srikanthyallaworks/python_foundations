"""


"""

import random
from enum import Enum
from dice import Die,Cup

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
  

  def won(self):
    self.outcome= Outcome.Win
    print('Game Over: Won!')
  

  def lost(self):
    self.outcome= Outcome.Loss
    print('Game Over: Lost')
  

  def play(self):
    firstRoll = self.shoot()
    if firstRoll in [2,3,12]:
      self.lost()
    if firstRoll in [7,11]:
      self.won()
  
    while(self.outcome == Outcome.Undecided):
      result = self.shoot()
      if result==7:
        self.lost()
      if result==firstRoll:
        self.won()
        

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
    main()

