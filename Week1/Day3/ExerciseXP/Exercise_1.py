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
