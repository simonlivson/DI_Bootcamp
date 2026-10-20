# ===== Exercise_1.py =====
# Exercise 1: Cars
#
# What you learn here:
#   - Data types: turning a string into a list with split()
#   - len(), sorting (sorted / reverse)
#   - Loops and list comprehension with conditions (in / not in)
#   - set() to remove duplicates, ", ".join() to build a string
#   - Reversing a string with slicing [::-1]
#
# Instructions:
#   1. Copy the following string into your code:
#      "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
#   2. Convert it into a list using Python (don't do it by hand!).
#   3. Print out a message saying how many manufacturers/companies are in
#      the list.
#   4. Print the list of manufacturers in reverse/descending order (Z-A).
#   5. Using loops or list comprehension:
#      a. Find out how many manufacturers' names have the letter 'o' in them.
#      b. Find out how many manufacturers' names do not have the letter 'i'
#         in them.
#   6. Bonus: There are a few duplicates in this list:
#      ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
#      a. Remove these programmatically. (Hint: you can use set to help you).
#      b. Print out the companies without duplicates, in a comma-separated
#         string with no line-breaks (eg. "Acura, Alfa Romeo, Aston Martin, ..."),
#         also print out a message saying how many companies are now in the list.
#   7. Bonus: Print out the list of manufacturers in ascending order (A-Z),
#      but reverse the letters of each manufacturer's name.

# 1. The string
cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# 2. Convert it into a list
cars = cars_string.split(", ")
print(cars)

# 3. How many manufacturers
print(f"There are {len(cars)} manufacturers in the list.")

# 4. Reverse order (Z-A)
print(sorted(cars, reverse=True))

# 5.1 How many names have the letter 'o'
# ===== Way 1: Loop =====
count_o = 0
for car in cars:
    if 'o' in car:
        count_o += 1
print(f"{count_o} manufacturers have the letter 'o' in their name.")

# ===== Way 2: List comprehension =====
count_o2 = len([car for car in cars if 'o' in car])
print(f"{count_o2} manufacturers have the letter 'o' in their name.")

# 5.2 How many names do not have the letter 'i'
# ===== Way 1: Loop =====
count_no_i = 0
for car in cars:
    if 'i' not in car:
        count_no_i += 1
print(f"{count_no_i} manufacturers do not have the letter 'i' in their name.")

# ===== Way 2: List comprehension =====
count_no_i2 = len([car for car in cars if 'i' not in car])
print(f"{count_no_i2} manufacturers do not have the letter 'i' in their name.")

# 6. Bonus: remove duplicates
cars_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars_no_duplicates = list(set(cars_with_duplicates))
print(", ".join(cars_no_duplicates))
print(f"There are now {len(cars_no_duplicates)} companies in the list.")

# 7. Bonus: A-Z order with each name reversed
cars_reversed_names = [car[::-1] for car in sorted(cars)]
print(cars_reversed_names)
