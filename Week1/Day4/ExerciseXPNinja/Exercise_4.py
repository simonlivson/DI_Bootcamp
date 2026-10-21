# What we will learn:
# - Functions
#
# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?
#
# def insertion_sort(alist):
#    for index in range(1,len(alist)):
#      currentvalue = alist[index]
#      position = index
#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
#      alist[position]=currentvalue
# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

# What you learn here:
# - reading code before running it
# - a while loop inside a for loop
# - how a sorting algorithm works by itself (no .sort())
# - Way 2: wrapping it in a Day 4 function: *args, a safety check that returns a message, return

# ===== Way 1: the given code =====
def insertion_sort(alist):
# alist is the list to sort (it is changed in place)
    for index in range(1, len(alist)):
    # start from the 2nd item
        currentvalue = alist[index]
        # take the current item out
        position = index
        # where it is now
        while position > 0 and alist[position - 1] > currentvalue:
        # while the item on the left is bigger
            alist[position] = alist[position - 1]
            # move the bigger item one step right
            position = position - 1
            # go one step left
        alist[position] = currentvalue
        # put the current item in the free spot


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# the list from the instructions
insertion_sort(alist)
# sort it
print(alist)
# [17, 20, 26, 31, 44, 54, 55, 77, 93]


# ===== Way 2: Day 4 wrapper with *args + return =====
def sort_numbers(*numbers):
# numbers collects all the given numbers into a tuple
    if len(numbers) < 2:
    # safety check: nothing to sort with fewer than 2 numbers
        return "We need at least 2 numbers"
        # stop here and send back a message
    result = list(numbers)
    # tuples can't change, so make a list copy
    insertion_sort(result)
    # reuse the given function
    return result
    # send the sorted list back


print(sort_numbers(54, 26, 93, 17, 77, 31, 44, 55, 20))
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(sort_numbers(5))
# We need at least 2 numbers
