import sys


def foo(value):
    print(f'foo > Value: {value}')
    print(f'foo > refcount: {sys.getrefcount(value)}')
    value += 1


class Node:
    pass


def main():
    print('<main/>')
    a = 4
    print(f'main > refcount: {sys.getrefcount(a)}')
    foo(a)

    print(f'main > Value: {a}')

    print('</main>')


print('\n\n************** Begin *****************\n')
main()
print('\n\n************* Done! ******************\n')
