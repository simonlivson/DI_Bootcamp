# ===== Exercise_1.py =====
# Exercise 1: Concatenate lists
# Write code that concatenates two lists together without using the + sign.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)                    # [1, 2, 3, 4, 5, 6]


# ===== Exercise_2.py =====
# Exercise 2: Range of numbers
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        print(number)           # 1505, 1540, 1575 ... 2485


# ===== Exercise_3.py =====
# Exercise 3: Check the index
# Ask a user for their name, if their name is in the names list
# print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("Enter your name: ")

if name in names:
    print(names.index(name))


# ===== Exercise_4.py =====
# Exercise 4: Greatest Number
# Ask the user for 3 numbers and print the greatest number.

num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))
print(f"The greatest number is: {max(num1, num2, num3)}")


# ===== Exercise_5.py =====
# Exercise 5: The Alphabet
# Create a string of all the letters in the alphabet.
# Loop over each letter and print a message that contains the letter
# and whether its a vowel or a consonant.

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")


# ===== Exercise_6.py =====
# Exercise 6: Words and letters
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence
# of the letter variable in each word of the list.
# If the letter doesn't exist in one of the words, print a friendly message
# with the word and the letter.

words = []
for i in range(7):
    words.append(input(f"Enter word {i + 1}: "))

letter = input("Enter a single letter: ")

for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"'{letter}' first appears in '{word}' at index {index}")
    else:
        print(f"Sorry, the letter '{letter}' is not in '{word}'")


# ===== Exercise_7.py =====
# Exercise 7: Min, Max, Sum
# Create a list of numbers from one to one million and then use min() and max()
# to make sure your list actually starts at one and ends at one million.
# Use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))
print(min(numbers))             # 1
print(max(numbers))             # 1000000
print(sum(numbers))             # 500000500000


# ===== Exercise_8.py =====
# Exercise 8: List and Tuple
# Write a program which accepts a sequence of comma-separated numbers.
# Generate a list and a tuple which contain every number.
# Input: 34,67,55,33,12,98
# Output:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

user_input = input("Enter numbers separated by commas: ")
my_list = user_input.split(",")
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)


# ===== Exercise_9.py =====
# Exercise 9: Random number
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

won = 0
lost = 0

while True:
    guess = input("Guess a number from 1 to 9 (or 'quit' to stop): ")
    if guess == "quit":
        break

    random_number = random.randint(1, 9)
    if int(guess) == random_number:
        print("Winner")
        won += 1
    else:
        print(f"Better luck next time, it was {random_number}")
        lost += 1

print(f"Games won: {won}")
print(f"Games lost: {lost}")
