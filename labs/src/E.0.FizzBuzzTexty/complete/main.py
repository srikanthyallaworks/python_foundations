"""


"""


def toText(n):
    divisibleBy3 = n % 3 == 0
    divisibleBy5 = n % 5 == 0
    if divisibleBy3 and divisibleBy5:
        return "fizzbuzz"
    if divisibleBy3:
        return "fizz"
    if divisibleBy5:
        return "buzz"
    return str(n)


def main():
    for i in range(1,101):
        print(toText(i))


if __name__ == "__main__":
    main()


