# ==================== Exercise_1 ====================
# What we will learn:
# - Functions
#
# Exercise 1 : What's your name ?
# Instructions:
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it's omitted by the user, the name returned should only contain
# the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

# What you learn here:
# - optional parameter with a default value ("")
# - keyword arguments
# - .capitalize() to make the first letter big
# - early-return safety check that returns a message string
# - plain if / return instead of if / else
# - Way 2: *names + map + lambda to capitalize any amount of names

# ===== Way 1: default value + keyword arguments =====
def get_full_name(first_name, last_name, middle_name = ""):
# middle_name is optional: "" when it is not given
    if first_name == "" or last_name == "":
    # safety check: first and last name are required
        return "First and last name are required"
        # stop here and send back a message
    if middle_name == "":
    # no middle name given
        return f"{first_name.capitalize()} {last_name.capitalize()}"
        # stop here: Bruce Lee
    return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    # we only get here when there is a middle name: John Hooker Lee


print(get_full_name(first_name = "john", middle_name = "hooker", last_name = "lee"))
# John Hooker Lee
print(get_full_name(first_name = "bruce", last_name = "lee"))
# Bruce Lee
print(get_full_name(first_name = "", last_name = "lee"))
# First and last name are required


# ===== Way 2: *names + map + lambda =====
def get_full_name_args(*names):
# names collects all the given names into a tuple, in order
    if len(names) < 2:
    # safety check: we need at least a first and a last name
        return "We need at least a first and a last name"
        # stop here and send back a message
    return " ".join(map(lambda name: name.capitalize(), names))
    # capitalize every name, then glue them with spaces


print(get_full_name_args("john", "hooker", "lee"))
# John Hooker Lee
print(get_full_name_args("bruce", "lee"))
# Bruce Lee
print(get_full_name_args("bruce"))
# We need at least a first and a last name


# ==================== Exercise_2 ====================
# What we will learn:
# - Functions
#
# Exercise 2 : From English to Morse
# Instructions:
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and
# every word is separated with a slash /.

# What you learn here:
# - map + filter + lambda to translate in one line (Way 1, the main solution)
# - return + early-return safety check (empty text) that returns a message string
# - .get(key, default) so an unknown code doesn't crash
# - a dictionary as a translation table, .upper(), split() / " ".join()
# - Way 2: the older way, nested for loops

MORSE_TABLE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}
# letter -> morse code

REVERSE_TABLE = {}
# morse code -> letter (filled below)
for letter, code in MORSE_TABLE.items():
# go over every pair in the table
    REVERSE_TABLE[code] = letter
    # flip it: the code becomes the key


# ===== Way 1: map + filter + lambda =====
def english_to_morse(text):
# English -> morse in one line per word
    if text.strip() == "":
    # safety check
        return "No text given"
        # stop here and send back a message
    return " / ".join(map(lambda word: " ".join(map(lambda letter: MORSE_TABLE[letter], filter(lambda letter: letter in MORSE_TABLE, word))), text.upper().split()))
    # filter keeps known letters, inner map turns each into code, outer map does every word


def morse_to_english(morse):
# morse -> English with map
    if morse.strip() == "":
    # safety check
        return "No morse given"
        # stop here and send back a message
    return " ".join(map(lambda word: "".join(map(lambda code: REVERSE_TABLE.get(code, "?"), word.split())), morse.split("/")))
    # inner map turns each code into a letter, outer map does every word


morse = english_to_morse("Hello World")
# translate to morse
print(morse)
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_english(morse))
# HELLO WORLD
print(english_to_morse(""))
# No text given


# ===== Way 2: for loops =====
def english_to_morse_loop(text):
# English -> morse
    if text.strip() == "":
    # safety check: is there any text?
        return "No text given"
        # stop here and send back a message
    morse_words = []
    # one item per word
    for word in text.upper().split():
    # "HELLO", "WORLD"
        morse_letters = []
        # one item per letter
        for letter in word:
        # "H", "E", ...
            if letter in MORSE_TABLE:
            # skip signs we don't know
                morse_letters.append(MORSE_TABLE[letter])
                # add the code of that letter
        morse_words.append(" ".join(morse_letters))
        # letters separated by a space
    return " / ".join(morse_words)
    # words separated by a slash


def morse_to_english_loop(morse):
# morse -> English
    if morse.strip() == "":
    # safety check: is there any morse?
        return "No morse given"
        # stop here and send back a message
    english_words = []
    # one item per word
    for word in morse.split("/"):
    # every word is between slashes
        english_word = ""
        # build the word letter by letter
        for code in word.split():
        # every code is between spaces
            english_word += REVERSE_TABLE.get(code, "?")
            # unknown code -> "?" instead of a crash
        english_words.append(english_word)
        # save the word
    return " ".join(english_words)
    # words separated by a space


morse = english_to_morse_loop("Hello World")
# translate to morse
print(morse)
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_english_loop(morse))
# HELLO WORLD
print(english_to_morse_loop(""))
# No text given


# ==================== Exercise_3 ====================
# What we will learn:
# - Functions
#
# Exercise 3 : Box of stars
# Instructions:
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them,
# one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

# What you learn here:
# - *words: a function that takes any amount of arguments (they arrive as a tuple)
# - early-return safety check (no words) that returns a message string
# - result = words[0] + for e in words[1:] to find the longest word
# - max(map(len, words)) and reduce to do the same in one line
# - "*" * number to repeat a character
# - .ljust(width) to pad a word with spaces
# - building the lines in a list and "\n".join() them

from functools import reduce
# bring in reduce from the functools module


def make_box(longest, words):
# helper: builds the frame for words, using the longest length
    border = "*" * (longest + 4)
    # top and bottom line
    lines = [border]
    # start with the top line
    for word in words:
    # every word gets its own line
        lines.append(f"* {word.ljust(longest)} *")
        # pad the word with spaces so all lines are the same width
    lines.append(border)
    # bottom line
    return "\n".join(lines)
    # one string, a new line between each line


# ===== Way 1: result = words[0] loop =====
def box_printer(*words):
# words collects all the strings into a tuple
    if len(words) == 0:
    # safety check: did we get any words?
        return "We need at least 1 word"
        # stop here and send back a message
    longest = len(words[0])
    # start with the length of the first word
    for e in words[1:]:
    # every word after the first
        if len(e) > longest:
        # is this one longer?
            longest = len(e)
            # remember the new longest
    return make_box(longest, words)
    # build and send back the box


print(box_printer("Hello", "World", "in", "reallylongword", "a", "frame"))
# the box from the instructions
print(box_printer())
# We need at least 1 word


# ===== Way 2: max + map =====
def box_printer_map(*words):
# same box, longest found with max and map
    if len(words) == 0:
    # safety check
        return "We need at least 1 word"
        # stop here and send back a message
    longest = max(map(len, words))
    # map gives every length, max picks the biggest: 14
    return make_box(longest, words)
    # build and send back the box


print(box_printer_map("Hello", "World", "in", "reallylongword", "a", "frame"))
# same box


# ===== Way 3: reduce + lambda =====
def box_printer_reduce(*words):
# same box, longest found with reduce
    if len(words) == 0:
    # safety check
        return "We need at least 1 word"
        # stop here and send back a message
    longest = reduce(lambda result, e: len(e) if len(e) > result else result, words, 0)
    # start at 0, keep the bigger of (result so far, length of next word)
    return make_box(longest, words)
    # build and send back the box


print(box_printer_reduce("Hello", "World", "in", "reallylongword", "a", "frame"))
# same box


# ==================== Exercise_4 ====================
# What we will learn:
# - Functions
#
# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?
#
# def insertion_sort(alist):
#    for index in range(1,len(alist)):
#      currentvalue = alist[index]
#      position = index
#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
#      alist[position]=currentvalue
# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

# What you learn here:
# - reading code before running it
# - a while loop inside a for loop
# - how a sorting algorithm works by itself (no .sort())
# - Way 2: wrapping it in a Day 4 function: *args, a safety check that returns a message, return

# ===== Way 1: the given code =====
def insertion_sort(alist):
# alist is the list to sort (it is changed in place)
    for index in range(1, len(alist)):
    # start from the 2nd item
        currentvalue = alist[index]
        # take the current item out
        position = index
        # where it is now
        while position > 0 and alist[position - 1] > currentvalue:
        # while the item on the left is bigger
            alist[position] = alist[position - 1]
            # move the bigger item one step right
            position = position - 1
            # go one step left
        alist[position] = currentvalue
        # put the current item in the free spot


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# the list from the instructions
insertion_sort(alist)
# sort it
print(alist)
# [17, 20, 26, 31, 44, 54, 55, 77, 93]


# ===== Way 2: Day 4 wrapper with *args + return =====
def sort_numbers(*numbers):
# numbers collects all the given numbers into a tuple
    if len(numbers) < 2:
    # safety check: nothing to sort with fewer than 2 numbers
        return "We need at least 2 numbers"
        # stop here and send back a message
    result = list(numbers)
    # tuples can't change, so make a list copy
    insertion_sort(result)
    # reuse the given function
    return result
    # send the sorted list back


print(sort_numbers(54, 26, 93, 17, 77, 31, 44, 55, 20))
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(sort_numbers(5))
# We need at least 2 numbers
