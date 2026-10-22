# Daily Challenge: Advanced Algorithm
# Find all pairs of numbers in list_of_numbers that add up to target_number.
# Example: 1000 + 2728 = 3728, 1864 + 1864 = 3728
#
# What you learn here:
# - conditionals
# - loops
# - functions

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

# ===== Step 1: Remove the repeats =====

unique_numbers = set(list_of_numbers)
# a set keeps each number only once, and checking "x in a set" is very fast

# ===== Step 2: Find the pairs =====

def find_pairs(numbers, target):
# returns a list of all the pairs of numbers that add up to target

    pairs = []
    # the pairs we find go here

    for number in numbers:
    # go over each different number once

        partner = target - number
        # the number it needs, for example 3728 - 1000 = 2728

        if partner not in numbers:
        # safety check 1: the partner is not in our numbers

            continue
            # so skip to the next number

        if number > partner:
        # safety check 2: we already counted this pair from the other side
        # (1000 + 2728 is the same pair as 2728 + 1000)

            continue
            # skip it so every pair appears only once

        if number == partner and list_of_numbers.count(number) < 2:
        # safety check 3: 1864 + 1864 needs 1864 to be in the list at least twice

            continue
            # only once, so it can't pair with itself

        pairs.append((number, partner))
        # all checks passed: save the pair as a tuple

    return pairs
    # give back every pair we found

pairs = find_pairs(unique_numbers, target_number)
# run the function on our numbers and target

# ===== Step 3: Print the pairs =====

for number, partner in pairs:
# go over each pair and unpack the tuple into its 2 numbers

    print(f"{number} and {partner} sums to the target_number {target_number}")
    # print it in the same format as the example in the instructions

print(f"Found {len(pairs)} pairs in total.")
# at the end, say how many pairs there are