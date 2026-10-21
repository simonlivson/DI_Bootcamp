# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.
#
# Key Python Topics:
# - random module
# - random.randint() function
# - Conditional statements (if, else)
#
# Step 1: Import the random Module
# - At the beginning of your script, use import random to access the random number generation functions.
#
# Step 2: Define a Function with a Parameter
# - Create a function that accepts a number between 1 and 100 as a parameter.
#
# Step 3: Generate a Random Number
# - Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
#
# Step 4: Compare the Numbers
# - If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
#
# Step 5: Call the Function
# - Call the function with a number between 1 and 100.
#
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

# What you learn here:
# - import random
# - random.randint(low, high) gives a whole number from low to high
# - default parameters (low = 1, high = 100)
# - early-return safety check that returns a message string
# - plain if / return instead of if / else
# - return the message, then print it at the call
# - Way 2: the older way, if / else that prints

import random
# bring in the random module


# ===== Way 1: default values + early return =====
def compare_numbers(my_number, low = 1, high = 100):
# my_number is the user's guess, low and high have default values
    if my_number < low or my_number > high:
    # safety check: is the number outside the allowed range?
        return f"Number must be between {low} and {high}"
        # stop here and send back a message
    random_number = random.randint(low, high)
    # pick a random whole number between low and high
    if my_number == random_number:
    # did the guess match?
        return "Success!"
        # stop here and send back the success message
    return f"Fail! Your number: {my_number}, Random number: {random_number}"
    # we only get here when they did not match


print(compare_numbers(50))
# Success! or Fail! Your number: 50, Random number: ...
print(compare_numbers(150))
# Number must be between 1 and 100
print(compare_numbers(my_number = 5, low = 1, high = 10))
# keyword arguments: a smaller range, 1 to 10


# ===== Way 2: if / else with print =====
def compare_numbers_print(my_number):
# only the number, no defaults
    random_number = random.randint(1, 100)
    # pick a random whole number between 1 and 100
    if my_number == random_number:
    # did the guess match?
        print("Success!")
        # print success
    else:
    # they did not match
        print(f"Fail! Your number: {my_number}, Random number: {random_number}")
        # print fail and both numbers


compare_numbers_print(50)
# Success! or Fail! ...
