# Exercise 2: List of integers
# Analyze a list of 10 integers.

import random

# 1. Store the list of numbers in a variable
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a. The list of numbers, printed in a single line
print(numbers)

# 2b. The list sorted in descending order (largest to smallest)
print(sorted(numbers, reverse=True))

# 2c. The sum of all the numbers
print(sum(numbers))

# 3. A list containing the first and the last numbers
print([numbers[0], numbers[-1]])

# 4. A list of all the numbers greater than 50
greater_than_50 = []
for elem in numbers:
    if elem > 50:
        greater_than_50.append(elem)
print(greater_than_50)

# 5. A list of all the numbers smaller than 10
smaller_than_10 = []
for elem in numbers:
    if elem < 10:
        smaller_than_10.append(elem)
print(smaller_than_10)

# 6. All the numbers squared, e.g. for [1, 2, 3] print "1 4 9"
squared = ""
for elem in numbers:
    squared += str(elem ** 2) + " "
print(squared)

# 7. The numbers without any duplicates, and how many there are
no_duplicates = list(set(numbers))
print(no_duplicates)
print(len(no_duplicates))

# 8. The average of all the numbers
print(sum(numbers) / len(numbers))

# 9. The largest number
print(max(numbers))

# 10. The smallest number
print(min(numbers))

# 11. Bonus: sum, average, largest and smallest WITHOUT built-in functions
total = 0
count = 0
largest = numbers[0]
smallest = numbers[0]
for elem in numbers:
    total += elem
    count += 1
    if elem > largest:
        largest = elem
    if elem < smallest:
        smallest = elem
print(f"Sum: {total}")
print(f"Average: {total / count}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

# 12. Bonus: ask the user for 10 integers between -100 and 100
user_numbers = []
for i in range(10):
    user_numbers.append(int(input(f"Enter integer {i + 1} between -100 and 100: ")))
print(f"Your numbers: {user_numbers}")

# 13. Bonus: generate 10 random integers between -100 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(-100, 100))
print(f"10 random numbers: {random_numbers}")

# 14. Bonus: the amount of integers is random too (no smaller than 50)
amount = random.randint(50, 100)
random_amount_numbers = []
for i in range(amount):
    random_amount_numbers.append(random.randint(-100, 100))
print(f"{amount} random numbers: {random_amount_numbers}")

# 15. Bonus: Will the code work when the number of random numbers is not 10?
# Yes. Nothing assumes 10 numbers: loops go over every item, and
# len(), sum(), max() and min() work on a list of any length. Proof:
print(f"Count: {len(random_amount_numbers)}")
print(f"Sum: {sum(random_amount_numbers)}")
print(f"Average: {sum(random_amount_numbers) / len(random_amount_numbers)}")
print(f"Largest: {max(random_amount_numbers)}")
print(f"Smallest: {min(random_amount_numbers)}")
