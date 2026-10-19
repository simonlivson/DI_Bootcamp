# Exercise 8: List and Tuple
# Write a program which accepts a sequence of comma-separated numbers.
# Generate a list and a tuple which contain every number.
# Input: 34,67,55,33,12,98
# Output:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

user_input = input("Enter numbers separated by commas: ")
my_list = user_input.split(",")
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
