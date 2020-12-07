try:
  from .game import Game
except:
  from game import Game

def play_not_interactive():
  print("\nLet's play a game!")
  game = Game()
  game.select_initial(0)
  prize = game.select_final(1)
  print(f"You've won a {prize.name} worth ${prize.value}!!\n")

def main():
  play_not_interactive()

if __name__ == '__main__':
  main()
