# ===== Exercise_2.py =====
# Exercise 2: Birthdays Advanced
#
# What you learn here:
#   - Looping through dictionary keys to print all names
#   - Checking if a key exists (in) with if/else
#   - Printing an error message for a missing key
#
# Instructions:
#   1. Before asking the user to input a person's name print out all of the
#      names in the dictionary.
#   2. If the person that the user types is not found in the dictionary,
#      print an error message
#      ("Sorry, we don't have the birthday information for <person's name>")

birthdays2 = {
    "Simon": "1982/05/21",
    "Albert Einstein": "1879/03/14",
    "Marie Curie": "1867/11/07",
    "Isaac Newton": "1643/01/04",
    "Ada Lovelace": "1815/12/10"
}

print("Welcome to the birthday finder!")
print("You can look up the birthdays of the people in the list!")

print("These are the names in the list:")
for person in birthdays2.keys():
    print(person)

name2 = input("Enter a person's name: ")
if name2 in birthdays2:
    print(f"{name2}'s birthday is on {birthdays2[name2]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name2}")
