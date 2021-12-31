import time

min_possible = 1
max_possible = 100
guessed_correctly = False


def get_middle():
    spread = max_possible - min_possible
    return spread // 2 + min_possible


print("\n\n\n\nThink of a whole number between 1 and 100.")
print("And I'll try to guess it......")
time.sleep(2)
print("Ready?")

while not guessed_correctly:
    guess = get_middle()
    print(f"\nMy guess is...{guess}")
    print("Was I Right? Too low? Too high?")
    reply = input("[r/l/h]? ")
    if reply == "l":
        min_possible = guess + 1
    elif reply == "h":
        max_possible = guess - 1
    else:
        guessed_correctly = True

print("\nI won suckers!")
print("Hoooooo!")
