# Daily Challenge GOLD: Happy birthday
# Ask the user for their birthdate (DD/MM/YYYY) and display a cake.
# The number of candles is the last digit of the user's age (age 53 -> 3 candles).
# Bonus: if they were born in a leap year, display two cakes!

import datetime

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = birthdate.split("/")      # '21', '05', '1982'
day = int(day)
month = int(month)
year = int(year)

today = datetime.date.today()
age = today.year - year
if today.month < month or (today.month == month and today.day < day):
    age -= 1                                 # birthday hasn't come yet this year

candles = age % 10                           # last digit of the age: 44 -> 4

# the top of the cake is 11 characters wide: underscores around the candles
left = (11 - candles) // 2
right = 11 - candles - left
top = "_" * left + "i" * candles + "_" * right

cake = f"""       {top}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~"""

print(f"You are {age} years old, so you get {candles} candles!")
print(cake)

# Bonus: leap year -> two cakes
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("You were born in a leap year, here is a second cake!")
    print(cake)
