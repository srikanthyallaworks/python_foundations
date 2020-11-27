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


def proveWorth():
    for i in [n + 1 for n in range(99)]:
        print(toText(i))


if __name__ == "__main__":
    proveWorth()


