# ===== Exercise_1.py =====
# Exercise 1: Favorite Numbers
# Create a set called my_fav_numbers with your favorite numbers.
# Add two new numbers, then remove the last one you added.
# Create friend_fav_numbers, then combine both into our_fav_numbers.

my_fav_numbers = {7, 13, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(100)
my_fav_numbers.remove(100)          # remove the last number added
print(my_fav_numbers)
friend_fav_numbers = {3, 7, 50}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)              # 7 appears only once, sets have no duplicates


# ===== Exercise_2.py =====
# Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to it.

my_tuple = (1, 2, 3)
# my_tuple.append(4)                # AttributeError: tuples have no append
# my_tuple[0] = 10                  # TypeError: tuples are immutable
my_tuple2 = (4, 5)
my_tuple = my_tuple + my_tuple2     # not a change, a NEW tuple with the same name
print(my_tuple)                     # (1, 2, 3, 4, 5)


# ===== Exercise_3.py =====
# Exercise 3: List Manipulation
# Remove "Banana" and "Blueberries", add "Kiwi" to the end,
# add "Apples" to the beginning, count "Apples", then empty the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)                       # ['Apples', 'Apples', 'Oranges', 'Kiwi']
print(basket.count("Apples"))       # 2
basket.clear()
print(basket)                       # []


# ===== Exercise_4.py =====
# Exercise 4: Floats
# A float is a number with a decimal point (2.5), an integer is a whole number (2).
# Create the list 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without typing each number.

numbers = []
for elem in range(3, 11):           # 3, 4, 5 ... 10
    if elem % 2 == 0:
        numbers.append(elem // 2)   # even: whole result, stays an integer (2, 3, 4, 5)
    else:
        numbers.append(elem / 2)    # odd: result is a float (1.5, 2.5, 3.5, 4.5)
print(numbers)                      # [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]


# ===== Exercise_5.py =====
# Exercise 5: For Loop
# Print all numbers from 1 to 20, inclusive.
# Then print every number from 1 to 20 whose index is even.

for elem in range(1, 21):
    print(elem)
numbers = list(range(1, 21))
for i in range(len(numbers)):
    if i % 2 == 0:                  # the index is even
        print(numbers[i])           # 1, 3, 5 ... 19


# ===== Exercise_6.py =====
# Exercise 6: While Loop
# Ask the user for their name. Using while True, keep asking until
# the name is not digits and at least 3 letters long, then print "thank you".

while True:
    name = input("Enter your name: ")
    if name.isdigit() or len(name) < 3:
        print("Invalid name, try again")
    else:
        print("thank you")
        break


# ===== Exercise_7.py =====
# Exercise 7: Favorite Fruits
# Ask for favorite fruits separated by spaces, store them in a list.
# Ask for any fruit and say whether it is one of the favorites.

fav_fruits = input("Enter your favorite fruits, separated by spaces: ").split()
fruit = input("Enter the name of any fruit: ")
if fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# ===== Exercise_8.py =====
# Exercise 8: Pizza Toppings
# Ask for toppings one by one until the user types 'quit'.
# Print "Adding [topping] to your pizza." each time.
# At the end print all toppings and the total cost ($10 base + $2.50 per topping).

toppings = []
while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping == "quit":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + 2.5 * len(toppings)
print(f"Your toppings: {', '.join(toppings)}")
print(f"Total cost: ${total_cost}")


# ===== Exercise_9.py =====
# Exercise 9: Cinemax Tickets
# Ask for the age of each family member and calculate the total cost:
# under 3 is free, 3 to 12 is $10, over 12 is $15.

total_cost = 0
family_size = int(input("How many people in your family? "))
for i in range(family_size):
    age = int(input(f"Age of person {i + 1}: "))
    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"Total ticket cost: ${total_cost}")


# Bonus: a restricted movie, only for ages 16 to 21.
# Ask for each person's age, remove anyone not allowed, print the final list.

ages = []
group_size = int(input("How many people in the group? "))

for i in range(group_size):
    age = int(input(f"Age of person {i + 1}: "))
    ages.append(age)

for age in ages[:]:              # loop over a copy, so removing is safe
    if age < 16 or age > 21:
        ages.remove(age)

print(f"Final attendees: {ages}")
