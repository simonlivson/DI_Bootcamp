# Exercise 4: Frequency Of The Words
# Print the frequency of the words from the input.
# Input: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Output (one per line): 2:2  3.:1  3?:1  New:1  Python:5  Read:1  and:1 ...

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in sorted(set(words)):          # each word once, in sorted order
    print(f"{word}:{words.count(word)}")
