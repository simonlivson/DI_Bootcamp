# ===== TimeChallenge1.py =====
# Time Challenge #1: Reverse the Sentence
#
# What you learn here:
#   - input()
#   - split() a sentence into a list of words
#   - Looping backwards with range() / list slicing [::-1]
#   - " ".join() to rebuild the sentence
#
# Instructions:
#   Write a program to reverse the sentence wordwise.
#
#   Input:
#     You have entered a wrong domain
#   Output:
#     domain wrong a entered have You
#
#   You have 30 minutes to finish this challenge.
#
# Starter code (Python 2, raw_input() is input() in Python 3):
#   REverseinp= raw_input()
#   #write down your logic here
#   print(reversed)

inp = input()

# ===== Way 1: Loop =====
words = inp.split()
reversed_words = []
for i in range(len(words) - 1, -1, -1):
    reversed_words.append(words[i])
reversed = " ".join(reversed_words)
print(reversed)

# ===== Way 2: Slicing =====
reversed2 = " ".join(inp.split()[::-1])
print(reversed2)
