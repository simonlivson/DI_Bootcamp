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
