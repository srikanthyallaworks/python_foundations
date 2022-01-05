from dataclasses import dataclass
from random import Random
from typing import Final, Tuple

@dataclass(frozen=True)
class Die:
    """Represents a 'cubical' n-side die.

      _random is injectable for deterministic unit tests.
    """

    _side_count:int = 6
    _random:Random = Random()

    def roll(self) -> int:
        return self._random.randrange(1, self._side_count + 1)



class Cup:
    """Represents a cup that holds 1 or more dice."""
    _dice:Final[Tuple[Die,...]]

    def __init__(self, die_count=2, random:Random = Random()):
        self._dice = tuple(Die(6,random) for _ in range(die_count))

    def roll(self) -> int:
        return sum(die.roll() for die in self._dice)
