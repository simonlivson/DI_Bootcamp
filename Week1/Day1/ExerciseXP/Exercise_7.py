# Exercise 7: Odd or Even
# Write code that asks the user for a number
# and determines whether this number is odd or even.

number = int(input("Please write a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")