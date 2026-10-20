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
