from dataclasses import dataclass
from functools import reduce
from typing import Generic, TypeVar, Optional, Generator
from typing_extensions import Self

T = TypeVar("T")


@dataclass(frozen=True)
class Node(Generic[T]):
    """Node in a linked list

    Args:
        Generic ([type]): Type of thing to hold.
    """

    value: T
    tail: Optional[Self]


@dataclass()
class LinkedList(Generic[T]):
    head: Optional[Node[T]]

    def __get_items(self) -> Generator[T, None, None]:
        hed = self.head
        while hed != None:
            yield hed.value
            hed = hed.tail

    def __len__(self) -> int:
        return reduce(lambda count, _: count + 1, self.__get_items(), 0)
