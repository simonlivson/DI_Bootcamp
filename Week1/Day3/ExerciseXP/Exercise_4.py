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
