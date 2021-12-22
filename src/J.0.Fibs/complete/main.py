def is_even(value):
    """Returns a value indicating whether the 
    specified value is even

    Args:
        n (int): some number

    Returns:
        boolean: True means even; False means odd
    """
    return value % 2 == 0


def get_fib_sequence(limit):
    """Gets a list containing the terms of the fibonacci
    sequence up to and possibly including the specified max value.

    Args:
        max (int): Maximum size of term in the generated
          sequence

    Returns:
        list[int]: Fibonacci sequence
    """
    previous = 1
    current = 2
    terms = [previous]
    while current <= limit:
        terms.append(current)
        next_term = current + previous
        previous = current
        current = next_term
    return terms


def get_euler02_solution():
    """Gets the solution.

    Returns:
        int: Sum of even terms of the fibonacci 
        sequence below 4 million
    """
    limit = 4e6
    total = 0
    for term in get_fib_sequence(limit):
        if is_even(term):
            total += term
    return total


def main():
    print(f'Here is your answer: {get_euler02_solution()}')


if __name__ == "__main__":
    main()
