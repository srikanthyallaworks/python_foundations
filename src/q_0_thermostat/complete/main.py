from typing import Final, ClassVar


def get_id_generator(starting_point: int = 0):
    next_id = starting_point

    def get_next():
        nonlocal next_id
        current = next_id
        next_id = next_id + 1
        return current

    return get_next


class Customer:
    get_next_id:Final = get_id_generator()
    id:Final[int]

    def __init__(self, givenName, surname):
        self.id = Customer.get_next_id()
        self.givenName = givenName
        self.surname = surname

    def __repr__(self):
        return f'{{id: {self.id}, givenName:{self.givenName}, sn:{self.surname}}}'


def main():
    c0=Customer('joe','bloggs')
    print(c0)
    c0.id=100
    print(c0)
    #c1=Customer('jane','doe')
    #print(c1)


if __name__ == "__main__":
    main()
