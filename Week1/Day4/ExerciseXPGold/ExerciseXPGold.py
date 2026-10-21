# ==================== Exercise_1 ====================
# What we will learn:
# - Functions
#
# Exercise 1 : When will I retire ?
# Instructions:
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let's say retirement age is 67 for men, and 62 for women (born after April, 1947).
#
# 1. Create a function get_age(year, month, day)
#    Hard-code the current year and month in your code (there are better ways of doing this,
#    but for now it will be enough.)
# 2. After calculating the age of a person, the function should return the age (the age is an integer).
# 3. Create a function can_retire(gender, date_of_birth).
#    It should call the get_age function (with what arguments?) in order to receive an age.
#    Now it has all the information it needs in order to determine if the person with the given
#    gender and date of birth is able to retire or not.
# 4. Calculate. You may need to do a little more hard-coding here.
# 5. Return True if the person can retire, and False if he/she can't.
#
# Some Hints:
# 1. Ask for the user's gender as "m" or "f".
# 2. Ask for the user's date of birth in the form of "yyyy/mm/dd", eg. "1993/09/21".
# 3. Call can_retire to get a definite value for whether the person can or can't retire.
# 4. Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

# What you learn here:
# - hard-coded values (current year / month / day)
# - a function that calls another function
# - split("/") + map(int, ...) to turn "1993/09/21" into numbers in one line
# - early-return safety checks (gender, date format) that return a message string
# - plain if / return instead of elif / else
# - returning True / False

CURRENT_YEAR = 2026
# hard-coded current year
CURRENT_MONTH = 10
# hard-coded current month
CURRENT_DAY = 21
# hard-coded current day


def get_age(year, month, day):
# gives back the age as a whole number
    age = CURRENT_YEAR - year
    # age if the birthday already happened this year
    if month > CURRENT_MONTH or (month == CURRENT_MONTH and day > CURRENT_DAY):
    # birthday not reached yet this year
        age -= 1
        # so one year less
    return age
    # send the age back


def can_retire(gender, date_of_birth):
# gives back True / False, or a message if the input is wrong
    if gender != "m" and gender != "f":
    # safety check: gender must be m or f
        return "Gender must be m or f"
        # stop here and send back a message
    parts = date_of_birth.split("/")
    # "1993/09/21" -> ["1993", "09", "21"]
    if len(parts) != 3:
    # safety check: we need year, month and day
        return "Date must be in the form yyyy/mm/dd"
        # stop here and send back a message
    year, month, day = map(int, parts)
    # map does int() on every part: 1993, 9, 21
    age = get_age(year, month, day)
    # call the other function
    if gender == "m":
    # men retire at 67
        return age >= 67
        # True or False
    return age >= 62
    # we only get here for "f": women retire at 62


gender = input("Enter your gender (m/f): ")
# ask for the gender
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")
# ask for the date of birth
result = can_retire(gender, date_of_birth)
# True, False, or a message

if result == True:
# they can retire
    print("You can retire!")
    # show it
if result == False:
# they can't retire
    print("You can't retire yet.")
    # show it
if type(result) == str:
# we got a message back
    print(result)
    # show the message


# ==================== Exercise_2 ====================
# What we will learn:
# - Functions
#
# Exercise 2 : Sum
# Instructions:
# 1. Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
# Hint: treating our number as a int or a str at different points in our code may be helpful

# What you learn here:
# - sum() + map + lambda (Way 1, the main solution)
# - reduce (from functools import reduce) + lambda to add everything into one number
# - early-return safety check that returns a message string
# - str(x) * 2 -> "33" (repeat a string), int("33") -> 33 (back to a number)
# - Way 3 / 4: the older ways, total += in a loop and written out

from functools import reduce
# bring in reduce from the functools module


# ===== Way 1: sum + map + lambda =====
def sum_x_map(x):
# same result with sum and map
    if type(x) != int:
    # safety check
        return "X must be a whole number"
        # stop here and send back a message
    return sum(map(lambda i: int(str(x) * i), range(1, 5)))
    # map makes 3, 33, 333, 3333 and sum adds them


print(sum_x_map(3))
# 3702


# ===== Way 2: reduce + map + lambda =====
def sum_x_reduce(x):
# same result with reduce
    if type(x) != int:
    # safety check
        return "X must be a whole number"
        # stop here and send back a message
    return reduce(lambda result, e: result + e, map(lambda i: int(str(x) * i), range(1, 5)))
    # 3 + 33 = 36, 36 + 333 = 369, 369 + 3333 = 3702


print(sum_x_reduce(3))
# 3702


# ===== Way 3: Loop =====
def sum_x(x):
# gives back X + XX + XXX + XXXX
    if type(x) != int:
    # safety check: X must be a whole number
        return "X must be a whole number"
        # stop here and send back a message
    total = 0
    # start the total at 0
    for i in range(1, 5):
    # i = 1, 2, 3, 4
        total += int(str(x) * i)
        # "3" * 2 = "33" -> 33, add it to the total
    return total
    # send the total back


print(sum_x(3))
# 3702
print(sum_x("3"))
# X must be a whole number


# ===== Way 4: Written out =====
def sum_x_written(x):
# every part written by hand
    if type(x) != int:
    # safety check
        return "X must be a whole number"
        # stop here and send back a message
    text = str(x)
    # 3 -> "3"
    return int(text) + int(text * 2) + int(text * 3) + int(text * 4)
    # 3 + 33 + 333 + 3333


print(sum_x_written(3))
# 3702


# ==================== Exercise_3 ====================
# What we will learn:
# - Functions
#
# Exercise 3 : Double Dice
# Instructions:
# 1. Create a function that will simulate the rolling of a dice. Call it throw_dice.
#    It should return an integer between 1 and 6.
# 2. Create a function called throw_until_doubles.
#    1. It should keep throwing 2 dice (using your throw_dice function) until they both land on the
#       same number, ie. until we reach doubles.
#       For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
#    2. This function should return the number of times it threw the dice in total.
#       In the example above, it should return 3.
# 3. Create a main function.
#    It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times),
#    and store the results of those function calls (in other words, how many throws it took until
#    doubles were thrown, each time) in a collection. (What kind of collection? Read below to
#    understand what we will need the data for, and this should help you decide which data
#    structure to use).
# 4. After the 100 doubles are thrown, print out a message telling the user how many throws it took
#    in total to reach 100 doubles.
# 5. Also print out a message telling the user the average amount of throws it took to reach doubles.
#    Round this off to 2 decimal places.
# 6. For example:
#    If the results of the throws were as follows (your code would do 100 doubles, not just 3):
#    1. (1, 2), (3, 1), (5, 5)
#    2. (3, 3)
#    3. (2, 4), (1, 2), (3, 4), (2, 2)
#    Then my output would show something like this:
#    Total throws: 8
#    Average throws to reach doubles: 2.67.

# What you learn here:
# - random.randint(1, sides) for a dice, with a default parameter (sides = 6)
# - while loop that stops when a condition is met (doubles)
# - counter += 1
# - a list as the collection, then sum() / len() for the average
# - default parameter (times = 100) + early-return safety check with a message
# - round(x, 2)

import random
# bring in the random module


def throw_dice(sides = 6):
# one dice throw, 6 sides unless told otherwise
    return random.randint(1, sides)
    # a whole number from 1 to sides


def throw_until_doubles():
# keep throwing 2 dice until they match, give back how many throws it took
    count = 0
    # no throws yet
    while True:
    # keep going until we return
        dice1 = throw_dice()
        # first dice
        dice2 = throw_dice()
        # second dice
        count += 1
        # one more throw
        if dice1 == dice2:
        # doubles?
            return count
            # stop and send back the number of throws


def main(times = 100):
# throw doubles "times" times and give back the summary
    if times < 1:
    # safety check: we need at least 1 round
        return "We need at least 1 round"
        # stop here and send back a message
    results = []
    # the collection: one number per round
    for i in range(times):
    # repeat "times" times
        results.append(throw_until_doubles())
        # save how many throws this round took
    total_throws = sum(results)
    # add all the rounds together
    average = round(total_throws / len(results), 2)
    # average with 2 decimals
    return f"Total throws: {total_throws}\nAverage throws to reach doubles: {average}"
    # send back both lines


print(main())
# Total throws: ... / Average throws to reach doubles: ...
print(main(0))
# We need at least 1 round
