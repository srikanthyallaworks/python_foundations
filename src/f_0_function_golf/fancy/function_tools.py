from functools import reduce
import operator
from typing import Any, Callable, ParamSpec, Sequence, TypeVar, overload


def make_adder(quantity_to_add: int = 0) -> Callable[[int], int]:
    """Makes a function that adds the specified quantity to its argument.

    Example:
        add10 = make_adder(10)
        result = add10(18)
        print(result) # Prints 28

    Args:
        quantity_to_add (int, optional): number that the returned function will add to
        its argument. Defaults to 0.

    Returns:
        Callable[[int],int]: Function that adds a quantity to its argument.
    """
    return lambda x: x + quantity_to_add


#
#
#
#
#
#

Vector = tuple[int, int]


def sort_by_magnitude(vectors: Sequence[Vector]) -> Sequence[Vector]:
    """Sorts a sequence of 2D vectors by magnitude, biggest first.

     Note: Magnitude just means the length of the vector, using a**2+b**2 = c**2.
           So for the vector (2,2)--
               magnitude**2 == 2**2 + 2**2
               magnitude**2 == 8
               magnitude == 8 ** .5
               magnitude == 2.83.....

    Example:
      result = sort_by_magnitude([(1,1), (100,100), (4,2)])
      print(result)
      > [(100,100), (4,2), (1,1)]

    Args:
        vectors (List[Tuple[int,int]]): A list of vectors in tuple form.
    """

    def get_magnitude(v: Vector):
        return (v[0] * v[1]) ** 0.5

    return sorted(vectors, key=get_magnitude, reverse=True)


#
#
#
#
#
#


def add_all(*terms: int):
    """Takes an arbitrary number of numeric arguments and returns the sum.

    Example:
        add(1) # 1
        add(1,2) # 3
        add(1,2,3) # 6
        ...

    Returns:
        [number]: sum of all arguments
    """
    return reduce(operator.add, terms, 0)


#
#
#
#
#
#


Tp_a = TypeVar("Tp_a")
Tp_b = TypeVar("Tp_b")
Tp_c = TypeVar("Tp_c")
Tp_d = TypeVar("Tp_d")
Tp_e = TypeVar("Tp_e")
Tp_f = TypeVar("Tp_f")


@overload
def pipe(operations: tuple[Callable[[Tp_a], Tp_b]], argument: Tp_a) -> Tp_b:
    """..."""


@overload
def pipe(
    operations: tuple[Callable[[Tp_a], Tp_b], Callable[[Tp_b], Tp_c]], argument: Tp_a
) -> Tp_c:
    """..."""


@overload
def pipe(
    operations: tuple[
        Callable[[Tp_a], Tp_b], Callable[[Tp_b], Tp_c], Callable[[Tp_c], Tp_d]
    ],
    argument: Tp_a,
) -> Tp_d:
    """..."""


@overload
def pipe(
    operations: tuple[
        Callable[[Tp_a], Tp_b],
        Callable[[Tp_b], Tp_c],
        Callable[[Tp_c], Tp_d],
        Callable[[Tp_d], Tp_e],
    ],
    argument: Tp_a,
) -> Tp_e:
    """..."""


@overload
def pipe(
    operations: tuple[
        Callable[[Tp_a], Tp_b],
        Callable[[Tp_b], Tp_c],
        Callable[[Tp_c], Tp_d],
        Callable[[Tp_d], Tp_e],
        Callable[[Tp_e], Tp_f],
    ],
    argument: Tp_a,
) -> Tp_f:
    """..."""


def pipe(operations: Any, argument: Any):
    """Takes a list of functions and applies each one in order,
       passing the result to the next function in line.

    Args:
        operations: list of functions
        argument: Argument to pass in to the first function.

    Returns:
        The result of applying each function in order.
    """
    return reduce(lambda result, operation: operation(result), operations, argument)


#
#
#
#
#
#

Tc_a = ParamSpec("Tc_a")
Tc_b = TypeVar("Tc_b")
Tc_c = TypeVar("Tc_c")
Tc_d = TypeVar("Tc_d")
Tc_e = TypeVar("Tc_e")
Tc_f = TypeVar("Tc_f")
Tc_g = TypeVar("Tc_g")


@overload
def compose(
    Fa: Callable[Tc_a, Tc_b], Fb: Callable[[Tc_b], Tc_c]
) -> Callable[Tc_a, Tc_c]:
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """


@overload
def compose(
    Fa: Callable[Tc_a, Tc_b],
    Fb: Callable[[Tc_b], Tc_c],
    Fc: Callable[[Tc_c], Tc_d],
) -> Callable[Tc_a, Tc_d]:
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """


@overload
def compose(
    Fa: Callable[Tc_a, Tc_b],
    Fb: Callable[[Tc_b], Tc_c],
    Fc: Callable[[Tc_c], Tc_d],
    Fd: Callable[[Tc_d], Tc_e],
) -> Callable[Tc_a, Tc_e]:
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """


@overload
def compose(
    Fa: Callable[Tc_a, Tc_b],
    Fb: Callable[[Tc_b], Tc_c],
    Fc: Callable[[Tc_c], Tc_d],
    Fd: Callable[[Tc_d], Tc_e],
    Fe: Callable[[Tc_e], Tc_f],
) -> Callable[Tc_a, Tc_f]:
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """


@overload
def compose(
    Fa: Callable[Tc_a, Tc_b],
    Fb: Callable[[Tc_b], Tc_c],
    Fc: Callable[[Tc_c], Tc_d],
    Fd: Callable[[Tc_d], Tc_e],
    Fe: Callable[[Tc_e], Tc_f],
    Ff: Callable[[Tc_f], Tc_g],
) -> Callable[Tc_a, Tc_g]:
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """


def compose(*operations):
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """

    def compose_binary(
        Fa: Callable[[Tc_a], Tc_b], Fb: Callable[[Tc_b], Tc_c]
    ) -> Callable[[Tc_a], Tc_c]:
        return lambda a: Fb(Fa(a))

    return reduce(compose_binary, operations)
