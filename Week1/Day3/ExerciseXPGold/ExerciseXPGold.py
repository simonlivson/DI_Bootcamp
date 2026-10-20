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

# ===== Exercise_4.py =====
# Exercise 4: Fruit Shop
#
# What you learn here:
#   - Looping through a dictionary with .items()
#   - Nested dictionaries (a dictionary inside a dictionary)
#   - Calculations (price * stock) and adding up a total
#
# Instructions:
#   items = {
#       "banana": 4,
#       "apple": 2,
#       "orange": 1.5,
#       "pear": 3
#   }
#   1. Using the dictionary above, each key-value pair represents an item and
#      its price - print all the items and their prices in a sentence.
#   2. Using the dictionary below, each value are dictionaries containing both
#      the price and the amount of items in stock - write some code to
#      calculate how much it would cost to buy everything in stock.
#   items = {
#       "banana": {"price": 4 , "stock":10},
#       "apple": {"price": 2, "stock":5},
#       "orange": {"price": 1.5 , "stock":24},
#       "pear": {"price": 3 , "stock":1}
#   }

# Part 1: print all items and their prices
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for (item, price) in items.items():
    print(f"A {item} costs ${price}.")

# Part 2: cost of buying everything in stock
items2 = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for (item, info) in items2.items():
    total_cost += info["price"] * info["stock"]
print(f"Buying everything in stock costs ${total_cost}.")
