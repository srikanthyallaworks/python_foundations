from dataclasses import dataclass
import random
from typing import Final, Tuple

@dataclass(frozen=True)
class Die:
    """Represents a 'cubical' n-side die."""

    _side_count:int = 6

    def roll(self) -> int:
        return random.randrange(1, self._side_count + 1)



class Cup:
    """Represents a cup that holds 1 or more dice."""
    _dice:Final[Tuple[Die,...]]

    def __init__(self, die_count=2):
        self._dice = tuple(Die() for _ in range(die_count))

    def roll(self) -> int:
        return sum(die.roll() for die in self._dice)
