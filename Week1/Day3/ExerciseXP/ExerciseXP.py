# ===== Exercise_1.py =====
# Exercise 1: Converting Lists into Dictionaries
#
# What you learn here:
#   - Creating dictionaries
#   - Zip function or dictionary comprehension
#
# Instructions:
#   You are given two lists. Convert them into a dictionary where the first
#   list contains the keys and the second list contains the corresponding values.
#
# Lists:
#   keys = ['Ten', 'Twenty', 'Thirty']
#   values = [10, 20, 30]
#
# Expected Output:
#   {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# ===== Way 1: Loop with range(len()) =====
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print(my_dict)

# ===== Way 2: Dictionary comprehension with zip =====
my_dict2 = {key: value for (key, value) in zip(keys, values)}
print(my_dict2)

# ===== Way 3: dict(zip()) =====
my_dict3 = dict(zip(keys, values))
print(my_dict3)

# ===== Exercise_2.py =====
# Exercise 2: Cinemax #2
#
# What you learn here:
#   - Looping through dictionaries
#   - Conditionals
#   - Calculations
#
# Instructions:
#   Write a program that calculates the total cost of movie tickets for a
#   family based on their ages.
#   - Family members' ages are stored in a dictionary.
#   - The ticket pricing rules are as follows:
#       Under 3 years old: Free
#       3 to 12 years old: $10
#       Over 12 years old: $15
#
# Family Data:
#   family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
#   - Loop through the family dictionary to calculate the total cost.
#   - Print the ticket price for each family member.
#   - Print the total cost at the end.
#
# Bonus:
#   Allow the user to input family members' names and ages, then calculate
#   the total ticket cost.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
for (name, age) in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name}: ${price}")
    total_cost += price
print(f"Total cost: ${total_cost}")

# Bonus: the user enters the family
family2 = {}
while True:
    name2 = input("Enter a name (or 'done' to finish): ")
    if name2 == 'done':
        break
    age2 = int(input(f"Enter {name2}'s age: "))
    family2[name2] = age2

total_cost2 = 0
for (name2, age2) in family2.items():
    if age2 < 3:
        price2 = 0
    elif age2 <= 12:
        price2 = 10
    else:
        price2 = 15
    print(f"{name2}: ${price2}")
    total_cost2 += price2
print(f"Total cost: ${total_cost2}")

# ===== Exercise_3.py =====
# Exercise 3: Zara
#
# What you learn here:
#   - Creating dictionaries
#   - Accessing and modifying dictionary elements
#   - Dictionary methods like .pop() and .update()
#
# Instructions:
#   Create and manipulate a dictionary that contains information about the
#   Zara brand.
#
# Brand Information:
#   name: Zara
#   creation_date: 1975
#   creator_name: Amancio Ortega Gaona
#   type_of_clothes: men, women, children, home
#   international_competitors: Gap, H&M, Benetton
#   number_stores: 7000
#   major_color:
#       France: blue,
#       Spain: red,
#       US: pink, green
#
#   1. Create a dictionary called brand with the provided data.
#   2. Modify and access the dictionary as follows:
#      - Change the value of number_stores to 2.
#      - Print a sentence describing Zara's clients using the type_of_clothes key.
#      - Add a new key country_creation with the value Spain.
#      - Check if international_competitors exists and, if so, add "Desigual"
#        to the list.
#      - Delete the creation_date key.
#      - Print the last item in international_competitors.
#      - Print the major colors in the US.
#      - Print the number of keys in the dictionary.
#      - Print all keys of the dictionary.
#
# Bonus:
#   Create another dictionary called more_on_zara with creation_date and
#   number_stores. Merge this dictionary with the original brand dictionary
#   and print the result.

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

# Change number_stores to 2
brand['number_stores'] = 2

# Sentence about Zara's clients
clothes = brand['type_of_clothes']
print(f"Zara's clients are {clothes[0]}, {clothes[1]}, {clothes[2]} and {clothes[3]}.")

# Add country_creation
brand['country_creation'] = 'Spain'

# Add Desigual if international_competitors exists
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Delete creation_date
del brand['creation_date']

# Last international competitor
print(brand['international_competitors'][-1])

# Major colors in the US
print(brand['major_color']['US'])

# Number of keys
print(len(brand))

# All keys
print(brand.keys())

# Bonus: merge more_on_zara into brand
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
brand.update(more_on_zara)
print(brand)

# ===== Exercise_4.py =====
# Exercise 4: Disney Characters
#
# What you learn here:
#   - Looping with indexes
#   - Dictionary creation
#   - Sorting
#
# Instructions:
#   You are given a list of Disney characters. Create three dictionaries
#   based on different patterns as shown below:
#
# Character List:
#   users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#
# Expected Results:
#   1. Create a dictionary that maps characters to their indices:
#      {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#   2. Create a dictionary that maps indices to characters:
#      {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#   3. Create a dictionary where characters are sorted alphabetically and
#      mapped to their indices:
#      {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to indices
# ===== Way 1: Loop with range(len()) =====
char_to_index = {}
for i in range(len(users)):
    char_to_index[users[i]] = i
print(char_to_index)

# ===== Way 2: Comprehension =====
char_to_index2 = {users[i]: i for i in range(len(users))}
print(char_to_index2)

# 2. Indices to characters
# ===== Way 1: Loop with range(len()) =====
index_to_char = {}
for i in range(len(users)):
    index_to_char[i] = users[i]
print(index_to_char)

# ===== Way 2: Comprehension =====
index_to_char2 = {i: users[i] for i in range(len(users))}
print(index_to_char2)

# 3. Sorted characters to indices
sorted_users = sorted(users)

# ===== Way 1: Loop with range(len()) =====
sorted_to_index = {}
for i in range(len(sorted_users)):
    sorted_to_index[sorted_users[i]] = i
print(sorted_to_index)

# ===== Way 2: Comprehension =====
sorted_to_index2 = {sorted_users[i]: i for i in range(len(sorted_users))}
print(sorted_to_index2)
