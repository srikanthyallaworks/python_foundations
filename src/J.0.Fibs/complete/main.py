def is_even(n):
  """Returns a value indicating whether the 
  specified value is even

  Args:
      n (int): some number

  Returns:
      boolean: True means even; False means odd
  """
  return n%2==0

def get_fib_sequence(max):
  """Gets a list containing the terms of the fibonacci
  sequence up to and possibly including the specified max value.

  Args:
      max (int): Maximum size of term in the generated
        sequence

  Returns:
      list[int]: Fibonacci sequence
  """
  previous = 1
  current = 2
  terms = [previous]
  while current<=max:
    terms.append(current)
    next = current + previous
    previous = current
    current = next
  return terms


def get_euler02_solution():
  """Gets the solution.

  Returns:
      int: Sum of even terms of the fibonacci 
      sequence below 4 million
  """
  limit = 4e6
  sum = 0
  for n in get_fib_sequence(limit):
    if is_even(n):
      sum += n
  return sum

def main():
  print(f'Here is your answer: {get_euler02_solution()}')

if __name__ == "__main__":
    main()
