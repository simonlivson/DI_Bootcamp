# Exercise 9: Random number
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

won = 0
lost = 0

while True:
    guess = input("Guess a number from 1 to 9 (or 'quit' to stop): ")
    if guess == "quit":
        break

    random_number = random.randint(1, 9)
    if int(guess) == random_number:
        print("Winner")
        won += 1
    else:
        print(f"Better luck next time, it was {random_number}")
        lost += 1

print(f"Games won: {won}")
print(f"Games lost: {lost}")
