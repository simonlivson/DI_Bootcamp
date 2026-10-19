# Exercise 1: Concatenate lists
# Write code that concatenates two lists together without using the + sign.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)                    # [1, 2, 3, 4, 5, 6]
