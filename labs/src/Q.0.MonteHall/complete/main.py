try:
  from .game import Game
except:
  from game import Game

def play_interactive():
  game = Game()

  print(f'{game}\nPick a door [1,2,3]')
  initial_door_no = int(input('? '))
  game.select_initial(initial_door_no-1)

  print(f'\nMonty reveals a goat:\n{game}')
  print('Switch or stick?')
  print('Make your final selection [1,2,3]')
  final_door_no = int(input('? '))
  prize = game.select_final(final_door_no-1)
  print(f"\nYou've won a {prize.name} worth ${prize.value}!!")


def main():
  print("\n\nLet's play a game!")
  play_interactive()
  print()

if __name__ == '__main__':
  main()
