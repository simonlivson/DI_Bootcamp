# Count occurence
# Write a program which takes a string and a character as an input,
# and finds out the number of occurrences the character has in the string.
#
# String: Programming is cool!
# Character: o
# 3
#
# String: This is a great example
# Character: y
# 0
#
# You have 15 minutes to finish this challenge

# What you learn here:
# - sum() + map + lambda, True counts as 1 (Way 1, the main solution)
# - filter + lambda + len() (Way 2)
# - functions with parameters, return and an early-return safety check that returns a message
# - the built-in string method .count() (Way 3)
# - Way 4: the older way, counter pattern count += 1 inside a for loop

# ===== Way 1: sum + map + lambda =====
def count_map(text, character):
# text and character are the parameters
    if len(character) != 1:
    # safety check
        return "Character must be exactly 1 letter"
        # stop here and send back a message
    return sum(map(lambda letter: letter == character, text))
    # map gives True / False for each letter, sum counts the Trues (True = 1)


# ===== Way 2: filter + lambda =====
def count_filter(text, character):
# text and character are the parameters
    if len(character) != 1:
    # safety check
        return "Character must be exactly 1 letter"
        # stop here and send back a message
    return len(list(filter(lambda letter: letter == character, text)))
    # filter keeps only matching letters, len counts them


# ===== Way 3: .count() =====
def count_method(text, character):
# text and character are the parameters
    if len(character) != 1:
    # safety check
        return "Character must be exactly 1 letter"
        # stop here and send back a message
    return text.count(character)
    # the built-in string method counts for us


# ===== Way 4: Loop =====
def count_loop(text, character):
# text and character are the parameters
    if len(character) != 1:
    # safety check: we need exactly 1 character
        return "Character must be exactly 1 letter"
        # stop here and send back a message
    count = 0
    # nothing counted yet
    for letter in text:
    # go over every letter
        if letter == character:
        # is it the one we look for?
            count += 1
            # count it
    return count
    # send the count back

text = input("String: ")
# e.g. Programming is cool!
character = input("Character: ")
# e.g. o

print(count_map(text, character))
# Way 1: 3
print(count_filter(text, character))
# Way 2: 3
print(count_method(text, character))
# Way 3: 3
print(count_loop(text, character))
# Way 4: 3
