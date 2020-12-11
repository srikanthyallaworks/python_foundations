min_possible=1
max_possible=100
guessed_correctly=False

def get_middle():
  spread = max_possible - min_possible
  return spread//2 + min_possible

print("Think of a whole number between 1 an 100.")
print("And I'll try to guess it.")
print("Ready?")

while not guessed_correctly:
  guess = get_middle()
  print(f'\nMy guess is...{guess}')
  print(f'Was I Right? Too low? Too high?')
  reply = input('[r/l/h]? ')
  if reply == 'l':
    min_possible=guess
  elif reply == 'h':
    max_possible=guess
  else:
    guessed_correctly=True

print('\nI won suckers!')
print('Hoooooo!')



