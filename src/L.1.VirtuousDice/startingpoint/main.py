
class Game:
  _playerName:str
  def __init__(self,playerName):
    self._playerName=playerName

  def play(self):
    print(f'New player: {self._playerName}!')
    print("TODO: Implement me.")


def main():
  print()
  game = Game('Lizzy')
  game.play()
  print()

if __name__ == "__main__":
  main()

