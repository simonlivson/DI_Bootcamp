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