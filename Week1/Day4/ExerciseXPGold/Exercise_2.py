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
