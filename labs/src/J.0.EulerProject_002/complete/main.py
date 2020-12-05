def is_even(n):
  return n%2==0

def get_fib_sequence(max):
  fibs = [1]
  previous = 1
  current = 2
  while current<=max:
    fibs.append(current)
    next = current + previous
    previous = current
    current = next
  return fibs

limit = 4e6

def get_euler02_solution():
  sum = 0
  for n in get_fib_sequence(limit):
    if is_even(n):
      sum += n
  return sum

def main():
  print(f'Here is your answer: {get_euler02_solution()}')

if __name__ == "__main__":
    main()
