
def toText(n):
    """Transforms this number to a fizbuzz message

    Args:
        n (int): number

    Returns:
        str: either a number, 'fizz', 'buzz', or 'fizzbuzz'
    """
    return str(n)


def main():
    for i in [1, 2, 3, 4, 5, 6, 8, 9, 10]:
        print(toText(i))


if __name__ == "__main__":
    main()
