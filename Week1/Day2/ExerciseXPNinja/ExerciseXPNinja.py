# ===== Exercise_1.py =====
# Exercise 1: Formula
# Calculate and print a value according to this formula:
# Q = Square root of [(2 * C * D) / H]
# C is 50. H is 30.
# Ask the user for a comma-separated string of numbers, use each number as D
# and print all the results.
# Example: input 100,150,180  ->  output 18,22,24

import math

C = 50
H = 30

user_input = input("Enter numbers separated by commas: ")   # 100,150,180
results = []

for elem in user_input.split(","):     # '100', '150', '180'
    D = int(elem)
    Q = int(math.sqrt((2 * C * D) / H))  # int() cuts off the decimals: 18.25 -> 18
    results.append(str(Q))               # join needs strings

print(",".join(results))                 # 18,22,24


# ===== Exercise_2.py =====
# Exercise 2: List of integers
# Analyze a list of 10 integers.

import random

# 1. Store the list of numbers in a variable
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a. The list of numbers, printed in a single line
print(numbers)

# 2b. The list sorted in descending order (largest to smallest)
print(sorted(numbers, reverse=True))

# 2c. The sum of all the numbers
print(sum(numbers))

# 3. A list containing the first and the last numbers
print([numbers[0], numbers[-1]])

# 4. A list of all the numbers greater than 50
greater_than_50 = []
for elem in numbers:
    if elem > 50:
        greater_than_50.append(elem)
print(greater_than_50)

# 5. A list of all the numbers smaller than 10
smaller_than_10 = []
for elem in numbers:
    if elem < 10:
        smaller_than_10.append(elem)
print(smaller_than_10)

# 6. All the numbers squared, e.g. for [1, 2, 3] print "1 4 9"
squared = ""
for elem in numbers:
    squared += str(elem ** 2) + " "
print(squared)

# 7. The numbers without any duplicates, and how many there are
no_duplicates = list(set(numbers))
print(no_duplicates)
print(len(no_duplicates))

# 8. The average of all the numbers
print(sum(numbers) / len(numbers))

# 9. The largest number
print(max(numbers))

# 10. The smallest number
print(min(numbers))

# 11. Bonus: sum, average, largest and smallest WITHOUT built-in functions
total = 0
count = 0
largest = numbers[0]
smallest = numbers[0]
for elem in numbers:
    total += elem
    count += 1
    if elem > largest:
        largest = elem
    if elem < smallest:
        smallest = elem
print(f"Sum: {total}")
print(f"Average: {total / count}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

# 12. Bonus: ask the user for 10 integers between -100 and 100
user_numbers = []
for i in range(10):
    user_numbers.append(int(input(f"Enter integer {i + 1} between -100 and 100: ")))
print(f"Your numbers: {user_numbers}")

# 13. Bonus: generate 10 random integers between -100 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(-100, 100))
print(f"10 random numbers: {random_numbers}")

# 14. Bonus: the amount of integers is random too (no smaller than 50)
amount = random.randint(50, 100)
random_amount_numbers = []
for i in range(amount):
    random_amount_numbers.append(random.randint(-100, 100))
print(f"{amount} random numbers: {random_amount_numbers}")

# 15. Bonus: Will the code work when the number of random numbers is not 10?
# Yes. Nothing assumes 10 numbers: loops go over every item, and
# len(), sum(), max() and min() work on a list of any length. Proof:
print(f"Count: {len(random_amount_numbers)}")
print(f"Sum: {sum(random_amount_numbers)}")
print(f"Average: {sum(random_amount_numbers) / len(random_amount_numbers)}")
print(f"Largest: {max(random_amount_numbers)}")
print(f"Smallest: {min(random_amount_numbers)}")


# ===== Exercise_3.py =====
# Exercise 3: Working on a paragraph
# Paste a paragraph of text and store it in a variable.
# Print how many characters, sentences, words and unique words it contains.
# Bonus: non-whitespace characters, average words per sentence, non-unique words.

paragraph = "Python is a popular programming language. It was created by Guido van Rossum and first released in 1991. Python is known for its simple and readable code. Many people use Python for data science and artificial intelligence."

characters = len(paragraph)
sentences = paragraph.count(".")          # each sentence ends with a period
words = paragraph.split()
unique_words = set(words)
non_whitespace = len(paragraph.replace(" ", ""))
average_words = len(words) / sentences
non_unique_words = len(words) - len(unique_words)

print(f"Characters: {characters}")
print(f"Sentences: {sentences}")
print(f"Words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Non-whitespace characters: {non_whitespace}")
print(f"Average words per sentence: {average_words}")
print(f"Non-unique words: {non_unique_words}")


# ===== Exercise_4.py =====
# Exercise 4: Frequency Of The Words
# Print the frequency of the words from the input.
# Input: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Output (one per line): 2:2  3.:1  3?:1  New:1  Python:5  Read:1  and:1 ...

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in sorted(set(words)):          # each word once, in sorted order
    print(f"{word}:{words.count(word)}")
