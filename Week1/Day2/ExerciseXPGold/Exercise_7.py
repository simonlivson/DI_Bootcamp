# Exercise 7: Min, Max, Sum
# Create a list of numbers from one to one million and then use min() and max()
# to make sure your list actually starts at one and ends at one million.
# Use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))
print(min(numbers))             # 1
print(max(numbers))             # 1000000
print(sum(numbers))             # 500000500000
