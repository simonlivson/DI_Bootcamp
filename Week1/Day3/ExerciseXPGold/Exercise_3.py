# ===== Exercise_3.py =====
# Exercise 3: Add Your Own Birthday
#
# What you learn here:
#   - Adding a new key-value pair to a dictionary from user input
#   - Looking up keys (including newly added ones)
#   - Conditionals with if/else
#
# Instructions:
#   Add this new code: before asking the user to input a person's name to
#   look up, ask the user to add a new birthday:
#   1. Ask the user for a person's name - store it in a variable.
#   2. Ask the user for this person's birthday (in the format "YYYY/MM/DD")
#      - store it in a variable.
#   3. Now add this new data into your dictionary.
#   4. Make sure that if the user types any name that exists in the
#      dictionary - including the name that he entered himself - the
#      corresponding birthday is found and displayed.

birthdays3 = {
    "Simon": "1982/05/21",
    "Albert Einstein": "1879/03/14",
    "Marie Curie": "1867/11/07",
    "Isaac Newton": "1643/01/04",
    "Ada Lovelace": "1815/12/10"
}

print("Welcome to the birthday finder!")
print("You can look up the birthdays of the people in the list!")

# Add a new birthday
new_name = input("Add a person's name: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")
birthdays3[new_name] = new_birthday

print("These are the names in the list:")
for person in birthdays3.keys():
    print(person)

name3 = input("Enter a person's name: ")
if name3 in birthdays3:
    print(f"{name3}'s birthday is on {birthdays3[name3]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name3}")
