limit = 4e6

def get_fibs():
  return [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def get_euler02_solution():
  return sum(get_fibs())

def main():
  print(f'Here is your answer: {get_euler02_solution()}')

if __name__ == "__main__":
    main()
