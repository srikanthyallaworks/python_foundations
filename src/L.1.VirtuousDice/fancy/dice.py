

import random


class Die:
    _symbols = {
        None: '?',
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅',
    }

    _side_count = 6

    def __init__(self):
        self._value = None

    def roll(self) -> int:
        self._value = random.randrange(1, Die._side_count+1)
        return self._value

    @property
    def value(self) -> int:
        return self._value

    def __str__(self):
        return Die._symbols[self._value]


class Cup:

    def __init__(self, die_count=2):
        self._dice = [Die() for i in range(die_count)]

    def roll(self) -> int:
        for die in self._dice:
            die.roll()
        return self.value

    @property
    def value(self) -> int:
        return sum([die.value for die in self._dice])

    def __str__(self):
        return ' '.join([str(die) for die in self._dice])
