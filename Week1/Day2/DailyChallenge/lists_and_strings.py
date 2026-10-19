# Daily Challenge: Lists & Strings

# ===== Challenge_1 =====
# Challenge 1: Multiples of a Number
# Ask the user for a number and a length.
# Generate a list of multiples of the number, stopping at the given length.
# Example: number 7, length 5  ->  [7, 14, 21, 28, 35]

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []
for i in range(1, length + 1):       # i = 1, 2, 3 ... length
    multiples.append(number * i)

print(multiples)


# ===== Challenge_2 =====
# Challenge 2: Remove Consecutive Duplicate Letters
# Ask the user for a string and remove consecutive duplicate letters.
# Example: "ppoeemm"  ->  "poem"
# Non-consecutive duplicates are allowed, e.g. "recursive" stays "recursive".

word = input("Enter a word: ")

new_word = ""
for letter in word:
    if new_word == "" or letter != new_word[-1]:   # first letter, or different from the last one added
        new_word += letter

print(new_word)
