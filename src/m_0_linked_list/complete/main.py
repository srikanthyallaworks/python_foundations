from node import LinkedList, Node


def main():
    last = Node[int](5, None)
    last_1 = Node(4, last)
    last_2 = Node(3, last_1)
    last_3 = Node("2", last_2)
    head = Node(1, last_3)
    llist = LinkedList(head)
    print(len(llist))


if __name__ == "__main__":
    main()
