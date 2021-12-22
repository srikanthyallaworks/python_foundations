def to_text(n):
    """Transforms this number to a fizbuzz message

    Args:
        n (int): number

    Returns:
        str: either a number, 'fizz', 'buzz', or 'fizzbuzz'
    """

    is_divisible_by_3 = n % 3 == 0
    is_divisible_by_5 = n % 5 == 0

    if is_divisible_by_3 and is_divisible_by_5:
        return "fizzbuzz"

    if is_divisible_by_3:
        return "fizz"

    if is_divisible_by_5:
        return "buzz"

    return str(n)


def main():
    for i in range(1, 101):
        print(to_text(i))


if __name__ == "__main__":
    main()
