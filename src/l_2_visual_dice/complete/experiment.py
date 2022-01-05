from typing import Tuple
from collections import Counter
from dataclasses import dataclass

from dice import Cup


@dataclass(frozen=True)
class DataPoint:
    sum: int
    roll_count: int


ExperimentResult = Tuple[DataPoint, ...]


def get_results(dice_count=10, roll_count=500) -> ExperimentResult:
    cup = Cup(dice_count)
    raw_data = [cup.roll() for _ in range(roll_count)]
    data_points = [DataPoint(s, rc) for s, rc in Counter(raw_data).items()]
    sorted_points = sorted(data_points, key=lambda dp: dp.sum)
    return tuple(sorted_points)
