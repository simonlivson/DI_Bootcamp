# Exercise 1: Formula
# Calculate and print a value according to this formula:
# Q = Square root of [(2 * C * D) / H]
# C is 50. H is 30.
# Ask the user for a comma-separated string of numbers, use each number as D
# and print all the results.
# Example: input 100,150,180  ->  output 18,22,24

import math

C = 50
H = 30

user_input = input("Enter numbers separated by commas: ")   # 100,150,180
results = []

for elem in user_input.split(","):     # '100', '150', '180'
    D = int(elem)
    Q = int(math.sqrt((2 * C * D) / H))  # int() cuts off the decimals: 18.25 -> 18
    results.append(str(Q))               # join needs strings

print(",".join(results))                 # 18,22,24
