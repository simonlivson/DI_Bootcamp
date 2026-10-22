# Daily Challenge: Challenges
# Challenge 1: Sorting
# Input words separated by commas, print them sorted, still comma separated.
# Steps: input -> split -> sort -> join -> print
# Example: without,hello,bag,world -> bag,hello,without,world
#
# Challenge 2: Longest Word
# A function that returns the longest word in a sentence (first one if tied).
# Punctuation counts as part of the word.
# Steps: define function -> split -> set variables -> loop -> compare lengths -> return
# longest_word("Margaret's toy is a pretty doll.") -> "Margaret's"
# longest_word("A thing of beauty is a joy forever.") -> "forever."
# longest_word("Forgetfulness is by all means powerless!") -> "Forgetfulness"
#
# What you learn here:
# - strings and .split()
# - lists and sorting
# - for loops and if
# - len()
# - functions

# ===== Challenge 1: Sorting =====

words = input("Enter words separated by commas: ")
# Step 1: get the words as one string, for example "without,hello,bag,world"

word_list = words.split(",")
# Step 2: split at every comma into a list: ["without", "hello", "bag", "world"]

word_list.sort()
# Step 3: sort the list in alphabetical order: ["bag", "hello", "without", "world"]

result = ",".join(word_list)
# Step 4: join the list back into one string, with a comma between the words

print(result)
# Step 5: print the result: bag,hello,without,world


# ===== Challenge 2: Longest Word =====

def longest_word(sentence):
# Step 1: a function that takes a sentence (a string)

    words = sentence.split()
    # Step 2: split at the spaces into a list of words (punctuation stays in the word)

    longest = ""
    # Step 3: the longest word so far; empty at the start

    for word in words:
    # Step 4: go over each word

        if len(word) > len(longest):
        # Step 5: is this word longer than the longest so far?
        # (> and not >=, so on a tie the first word stays)

            longest = word
            # it is longer, so it becomes the new longest

    return longest
    # Step 6: give back the longest word

print(longest_word("Margaret's toy is a pretty doll."))
# should print Margaret's

print(longest_word("A thing of beauty is a joy forever."))
# should print forever.

print(longest_word("Forgetfulness is by all means powerless!"))
# should print Forgetfulness
