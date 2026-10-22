# Challenges #2
# Exercise 1: Draw these patterns with for loops:
#
#   *          *        *
#  ***        **        **
# *****      ***        ***
#           ****        ****
#          *****        *****
#                       *****
#                        ****
#                         ***
#                          **
#                           *
#
# Exercise 2: Before running the code below, comment each line,
# write each variable's values as they change, the final output,
# and what the program is for.
#
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)
#
# What you learn here:
# - conditionals
# - loops (nested for loops)
# - functions

# ===== Exercise 1, Pattern 1: Pyramid =====

for i in range(1, 4):
# i is the row number: 1, 2, 3

    print(" " * (3 - i) + "*" * (2 * i - 1))
    # spaces push the stars to the middle (2, 1, 0 spaces)
    # stars grow by 2 each row (1, 3, 5)


# ===== Exercise 1, Pattern 2: Right triangle =====

for i in range(1, 6):
# i is the row number: 1 to 5

    print(" " * (5 - i) + "*" * i)
    # fewer spaces each row (4, 3, 2, 1, 0) and more stars (1 to 5)


# ===== Exercise 1, Pattern 3: Two triangles =====

for i in range(1, 6):
# first half: rows 1 to 5

    print("*" * i)
    # 1, 2, 3, 4, 5 stars, starting at the left

for i in range(5, 0, -1):
# second half: i counts down 5, 4, 3, 2, 1 (the -1 is the step)

    print(" " * (5 - i) + "*" * i)
    # more spaces each row (0 to 4) and fewer stars (5 to 1)


# ===== Exercise 2: Analyse the code =====

my_list = [2, 24, 12, 354, 233]
# the list to work on

for i in range(len(my_list) - 1):
# i goes 0, 1, 2, 3: the position we want to fill with the smallest remaining number

    minimum = i
    # guess that the smallest number is at position i

    for j in range(i + 1, len(my_list)):
    # j checks every position after i

        if (my_list[j] < my_list[minimum]):
        # found a smaller number than our current smallest?

            minimum = j
            # remember its position

            if (minimum != i):
            # the smallest is not already at position i

                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
                # swap the two numbers

print(my_list)
# [2, 12, 24, 233, 354]

# Variable changes:
# i = 0: minimum = 0 (2). j = 1 to 4: 24, 12, 354, 233 are all bigger than 2.
#        No swap. List: [2, 24, 12, 354, 233]
# i = 1: minimum = 1 (24). j = 2: 12 < 24, so minimum = 2, swap 24 and 12.
#        List: [2, 12, 24, 354, 233]. j = 3: 354 < 24? No. j = 4: 233 < 24? No.
# i = 2: minimum = 2 (24). j = 3: 354 < 24? No. j = 4: 233 < 24? No.
#        No swap. List: [2, 12, 24, 354, 233]
# i = 3: minimum = 3 (354). j = 4: 233 < 354, so minimum = 4, swap 354 and 233.
#        List: [2, 12, 24, 233, 354]
#
# Final output: [2, 12, 24, 233, 354]
# Purpose: it sorts the list from smallest to biggest (this is called "selection sort").

