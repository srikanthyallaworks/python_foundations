
import random

try:
  from .game import Game, Door, DoorState
except:
  from game import Game, Door, DoorState


def get_strategies(): 
  """Gets a map of name: callable
  """

  def sticker(doors):
    """Stays with the door initially chosen
    """
    for door_number,door in enumerate(doors):
      if door.state==DoorState.InitialSelection:
        return door_number
    raise Exception("Couldn't find the door I chose")
 
  def swapper(doors):
    """Switches final selection to the other closed door
    """
    for door_number,door in enumerate(doors):
      if door.state==DoorState.Closed:
        return door_number
    raise Exception("Couldn't find the door I chose")
 
  def randomr(doors):
    """Randomly chooses a closed door
    """
    if random.random() > .5:
      return sticker(doors)
    return swapper(doors)

  strategies = [
    sticker,
    randomr,
    swapper
  ]
  return {s.__name__:s for s in strategies}
    

def play_simulation(chooser):
  game = Game()
  initial_selection = random.choice([0,1,2])
  game.select_initial(initial_selection)

  final_selection = chooser(game._doors)
  prize = game.select_final(final_selection)
  return prize.value


def test_strategies(game_count=100):
  strategies=get_strategies()
  winnings={k:0 for k in strategies}

  for i in range(game_count):
    for k in strategies:
      winnings[k]+=play_simulation(strategies[k])

  return winnings




def main():
  results = test_strategies()
  print('\nResults:')
  for n,v in results.items():
    print(f'\t{n}:${v}')

if __name__ == '__main__':
  main()

