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
