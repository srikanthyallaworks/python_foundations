from functools import reduce
import operator


def make_adder(quantity_to_add=0):
    """ Makes a function that adds the specified quantity to its argument.

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


def sort_by_magnitude(vectors):
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

    def get_magnitude(v):
        return (v[0] * v[1])**.5

    return sorted(vectors, key=get_magnitude, reverse=True)


def add_all(*terms):
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


def pipe(operations, argument):
    """Takes a list of functions and applies each one in order,
       passing the result to the next function in line.

    Args:
        operations: list of functions
        argument: Argument to pass in to the first function.

    Returns:
        The result of applying each function in order.
    """
    return reduce(lambda result, operation: operation(result), operations, argument)


def compose(operations):
    """Takes a list of functions, returning a new function
       that takes an argument and applies each function in order.

    Args:
        operations: 2 or more functions.
    """
    return lambda argument: reduce(lambda result, operation: operation(result), operations, argument)
