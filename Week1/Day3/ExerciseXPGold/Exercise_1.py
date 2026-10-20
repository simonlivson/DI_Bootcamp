# ===== Exercise_1.py =====
# Exercise 1: Birthday Look-up
#
# What you learn here:
#   - Data types (strings in a dictionary)
#   - Creating a dictionary and reading a value by its key
#   - input() and printing a formatted message
#
# Instructions:
#   1. Create a variable called birthdays. Its value should be a dictionary.
#   2. Initialize this variable with birthdays of 5 people of your choice.
#      For each entry in the dictionary, the key should be the person's name,
#      and the value should be their birthday.
#      Tip: Use the format "YYYY/MM/DD".
#   3. Print a welcome message for the user. Then tell them:
#      "You can look up the birthdays of the people in the list!"
#   4. Ask the user to give you a person's name and store the answer in a
#      variable.
#   5. Get the birthday of the name provided by the user.
#   6. Print out the birthday with a nicely-formatted message.

birthdays = {
    "Simon": "1982/05/21",
    "Albert Einstein": "1879/03/14",
    "Marie Curie": "1867/11/07",
    "Isaac Newton": "1643/01/04",
    "Ada Lovelace": "1815/12/10"
}

print("Welcome to the birthday finder!")
print("You can look up the birthdays of the people in the list!")

name = input("Enter a person's name: ")
birthday = birthdays[name]
print(f"{name}'s birthday is on {birthday}.")
