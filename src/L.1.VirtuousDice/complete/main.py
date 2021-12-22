from dice import Cup


class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.outcome = "Undecided"
        self._first_roll = 0
        self.cup = Cup()

    def shoot(self):
        value = self.cup.roll()
        print(f'{self.player_name} rolls a {value}')
        return value

    def finish_game(self, outcome):
        self.outcome = outcome
        print(f'Game Over: {outcome} for {self.player_name}!')

    def do_first_roll(self):
        result = self.shoot()
        if result in [2, 3, 12]:
            self.finish_game("Loss")
        if result in [7, 11]:
            self.finish_game("Win")
        self._first_roll = result

    def do_next_roll(self):
        result = self.shoot()
        if result == 7:
            self.finish_game("Loss")
        if result == self._first_roll:
            self.finish_game("Win")

    def play(self):
        self.do_first_roll()
        while self.outcome == "Undecided":
            self.do_next_roll()


def main():
    print()
    game = Game('Lizzy')
    game.play()
    print()


if __name__ == "__main__":
    main()
