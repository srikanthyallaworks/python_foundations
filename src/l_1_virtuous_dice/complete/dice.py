import random


class Die:
    """Represents a cubical 6-side die."""

    _side_count = 6

    def __init__(self):
        self._value = None

    def roll(self) -> int:
        self._value = random.randrange(1, Die._side_count + 1)
        return self._value


class Cup:
    """Represents a cup that holds 1 or more dice."""

    def __init__(self, die_count=2):
        self._dice = [Die() for i in range(die_count)]

    def roll(self) -> int:
        return sum([die.roll() for die in self._dice])
