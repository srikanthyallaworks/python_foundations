from typing import Tuple
from collections import Counter
from dataclasses import dataclass
from dice import Cup


@dataclass(frozen=True)
class DataPoint:
    sum: int
    frequency: int


Results = Tuple[DataPoint, ...]


@dataclass(frozen=True)
class Parameters:
    """Experiment parameters
    """
    dice_count: int
    roll_count: int


@dataclass(frozen=True)
class Experiment:
    name: str
    parameters: Parameters
    results: Results


def run_experiment(
    name: str, parameters: Parameters = Parameters(10, 50000)
) -> Experiment:
    cup = Cup(parameters.dice_count)
    raw_data = (cup.roll() for _ in range(parameters.roll_count))
    data_points = (DataPoint(s, rc) for s, rc in Counter(raw_data).items())
    sorted_points = sorted(data_points, key=lambda dp: dp.sum)
    return Experiment(name, parameters, tuple(sorted_points))
