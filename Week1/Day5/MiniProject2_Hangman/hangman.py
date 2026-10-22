# Mini-Project #2: Hangman
# The computer picks a random word and shows a star for each letter.
# The player guesses one letter at a time:
# - If it is in the word, show it in every correct position.
# - If not, add a body part (head, body, left arm, right arm, left leg, right leg).
# The game ends when the word is solved or all 6 body parts are drawn.
# The same letter can't be guessed twice.
#
# What you learn here:
# - conditionals
# - loops
# - functions
# - modules (random)

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

# ===== Step 1: Show the word as stars =====

guessed = []
# a list of every letter the player has guessed so far (empty at the start)

def show_word():
# builds the word as the player sees it: guessed letters shown, the rest as *

    display = ""
    # start with an empty string

    for letter in word:
    # go over each letter of the secret word

        if letter in guessed or letter == " ":
        # the letter was guessed, or it is the space in "credit card"

            display += letter
            # show it as it is

        else:
        # the letter was not guessed yet

            display += "*"
            # hide it with a star

    return display
    # give back the finished string, for example "p*th*n"

# ===== Step 2: Get a letter from the player =====

def get_guess():
# asks for one letter until it is valid and new, then returns it

    while True:
    # keep asking until the guess is good

        letter = input("Guess a letter: ").lower()
        # ask for a letter; .lower() turns "A" into "a" so both count the same

        if len(letter) != 1 or not letter.isalpha():
        # safety check 1: it must be exactly one letter (not "ab", "5" or nothing)

            print("Please type one letter.")
            # tell the player what went wrong

            continue
            # ask again

        if letter in guessed:
        # safety check 2: the player can't guess the same letter twice

            print("You already guessed that letter.")
            # tell the player

            continue
            # ask again

        guessed.append(letter)
        # the guess is good: remember it in the guessed list

        return letter
        # give the letter back

# ===== Step 3: Check the guess =====

def check_guess(letter):
# returns True if the letter is in the word, otherwise False

    if letter in word:
    # "in" checks if the letter appears anywhere in the word

        print(f"Yes! '{letter}' is in the word.")
        # good guess message

        return True
        # stop here: the guess was right

    print(f"No, '{letter}' is not in the word.")
    # we only get here if the letter was not found

    return False
    # the guess was wrong

# ===== Step 4: Draw the body parts =====

body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
# the 6 parts, in the order they are added to the gallows

def show_gallows(mistakes):
# shows which body parts are on the gallows after this many wrong guesses

    parts_on = body_parts[:mistakes]
    # slicing: take the first parts, as many as the mistakes (2 mistakes = head, body)

    print(f"Gallows ({mistakes}/6): {parts_on}")
    # show how many parts are on and which ones

# ===== Step 5: The main game loop =====

def play():
# runs the whole game from start to end

    mistakes = 0
    # no wrong guesses at the start

    while mistakes < 6 and "*" in show_word():
    # keep playing while the man is not complete and there are still hidden letters

        print(show_word())
        # show the word with stars

        show_gallows(mistakes)
        # show the body parts so far

        letter = get_guess()
        # get a new, valid letter

        if not check_guess(letter):
        # the letter is not in the word

            mistakes += 1
            # add one body part

    if "*" not in show_word():
    # the loop ended and no stars are left: every letter was found

        print(f"You won! The word was: {word}")
        # winning message

        return
        # stop here so the losing message is not printed

    show_gallows(mistakes)
    # we only get here if the player lost: show the full gallows

    print(f"You lost! The word was: {word}")
    # losing message with the answer

play()
# start the game