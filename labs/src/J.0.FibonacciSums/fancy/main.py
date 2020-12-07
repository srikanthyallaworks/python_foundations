import itertools
import operator
import functools

limit = 4e6

def is_within_limit(n):
  return n<=limit

def is_even(n):
  return n%2==0

@functools.lru_cache(maxsize=None)
def get_fib_term(n:int)->int:
    if n < 2:
        return n
    return get_fib_term(n-1) + get_fib_term(n-2)

def get_fib_sequence():
  return (get_fib_term(n) for n in itertools.count())


def get_fib_sequence_alternative():
  previous = 1
  yield previous

  current = 2
  while True:
    yield current
    current,previous = current + previous,current


def get_even_fibs():
  return filter(is_even,get_fib_sequence())

def get_even_fibs_below_limit():
  return itertools.takewhile(is_within_limit, get_even_fibs())

def get_euler02_solution():
  return sum(get_even_fibs_below_limit())

def main():
  print(f'Here is your answer: {get_euler02_solution()}')

if __name__ == "__main__":
    main()
