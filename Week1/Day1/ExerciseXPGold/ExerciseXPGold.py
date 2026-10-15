# ===== Exercise_1.py =====
# Exercise 1: Hello World-I love python
# Print the following output in one line of code:
# Hello world (4 times)
# I love python (4 times)

print("Hello world\n" * 4 + "I love python\n" * 4)


# ===== Exercise_2.py =====
# Exercise 2: What is the Season?
# Ask the user to input a month (1 to 12).
# Display the season of the month received:
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input("Please enter a month (1 to 12): "))

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("That is not a month between 1 and 12")

