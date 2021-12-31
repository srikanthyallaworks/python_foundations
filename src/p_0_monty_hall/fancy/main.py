import random
from typing import Callable, Tuple
from game import Game, Door, DoorState

# Types for annotating functions
Doors = Tuple[Door, Door, Door]
DoorNumber = int
DoorChooser = Callable[[Doors], DoorNumber]


def choose_stick(doors: Doors) -> DoorNumber:
    """Stays with the door initially chosen"""
    for door_number, door in enumerate(doors):
        if door.state == DoorState.InitialSelection:
            return door_number
    raise Exception("Couldn't find the door I chose")


def choose_swap(doors: Doors) -> DoorNumber:
    """Switches final selection to the other closed door"""
    for door_number, door in enumerate(doors):
        if door.state == DoorState.Closed:
            return door_number
    raise Exception("Couldn't find the door I chose")


def choose_random(doors: Doors) -> DoorNumber:
    """Randomly chooses a closed door"""
    if random.random() > 0.5:
        return choose_stick(doors)
    return choose_swap(doors)


def play_simulation(chooser: DoorChooser):
    game = Game()
    initial_selection = random.choice([0, 1, 2])
    game.select_initial(initial_selection)

    final_selection = chooser(game.doors)
    prize = game.select_final(final_selection)
    return prize.value


def test_strategies(game_count=100):
    strategies = {
        "swapper": choose_swap,
        "sticker": choose_stick,
        "randomr": choose_random,
    }
    winnings = {label: 0 for label in strategies}

    for _ in range(game_count):
        for label, strategy in strategies.items():
            winnings[label] += play_simulation(strategy)

    return winnings


def main():
    results = test_strategies()
    print("\nResults:")
    for n, v in results.items():
        print(f"\t{n}:${v}")
    print()


if __name__ == "__main__":
    main()
