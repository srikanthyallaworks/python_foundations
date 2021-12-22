from itertools import tee
from collections import defaultdict
from typing import Iterable, TypeVar, Tuple


T = TypeVar('T')


def pairwise(iterable: Iterable[T]) -> Iterable[Tuple[T, T]]:
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def groupby(items, get_key):
    groups = defaultdict(lambda: [])
    for item in items:
        groups[get_key(item)].append(item)
    return groups.items()
