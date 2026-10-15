# Daily Challenge
# 1. Ask the user for a string that is exactly 10 characters long.
# 2. Check the length of the string:
#    - Less than 10 characters: print "String not long enough."
#    - More than 10 characters: print "String too long."
#    - Exactly 10 characters: print "Perfect string" and continue.
# 3. Print the first and last characters.
# 4. Using a for loop, build and print the string one character at a time:
#    the first character, then the first two, and so on, until the whole string.
# 5. Bonus: shuffle the characters and print the jumbled string (use random.shuffle).

import random

user_string = input("Please write a string of exactly 10 characters: ")

if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # First and last characters
    print(user_string[0])
    print(user_string[-1])

    # Build the string one character at a time
    built_string = ""
    for character in user_string:
        built_string = built_string + character
        print(built_string)

    # Bonus: shuffle the characters
    characters = list(user_string)
    random.shuffle(characters)
    jumbled_string = "".join(characters)
    print(jumbled_string)