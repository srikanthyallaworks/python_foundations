"""

# Project Euler #2

## Summary: 

[Project Euler](https://projecteuler.net/) is a great site for honing your programming skills while learning some math at the same time.

Here's [problem #2](https://projecteuler.net/problem=2):

  Each new term in the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is generated by adding the previous two terms.  

  By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


## Product Requirements: 
* Complete the generator function 
* Complete the generator function 
* Use a filter to get even numbers
* Use reduce to get the sum


## Hints
* Read up on [itertools](https://docs.python.org/3/library/itertools.html)

"""

def is_even(n):
  return n%2==0

def get_fibs(max):
  previous = 1
  yield previous

  current = 2
  while current<=max:
    yield current
    next = current + previous
    previous = current
    current = next

limit = 4e6
sum = 0

for n in get_fibs(limit):
  if is_even(n):
    sum = sum + n

print(f'Here is your answer: {sum}')
