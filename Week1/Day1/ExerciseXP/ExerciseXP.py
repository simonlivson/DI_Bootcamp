# ===== Exercise_1.py =====
# Exercise 1: Hello World
# Print the output using one line of code
print("Hello world\n" * 4)

# ===== Exercise_2.py =====
# Exercise 2: Some Math
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8)
print((99 ** 3) * 8)


# ===== Exercise_3.py =====
# Exercise 3: What is the output?
# Predict the output of the following code snippets.
# Comment what your guess is, then run the code and compare.
print(5 < 3)              # my guess: False
print(3 == 3)             # my guess: True
print(3 == "3")           # my guess: False
print("3" > 3)            # my guess: Error
print("Hello" == "hello") # my guess: False

# ===== Exercise_4.py =====
# Exercise 4: Your computer brand
# Create a variable called computer_brand whose value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer")

# ===== Exercise_5.py =====
# Exercise 5: Info
# Create a variable called name, and set its value to your name.
# Create a variable called age, and set its value to your age.
# Create a variable called shoe_size, and set its value to your shoe size.
# Create a variable called info and set its value to an interesting sentence about yourself.
# The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Simon"
age = 44
shoe_size = 46
info = f"Hi my name is {name}, and I am {age} years old. My shoe size is {shoe_size}.\n I was the Chief Rabbi of Finland"
print(info)


# ===== Exercise_6.py =====
# Exercise 6: A & B
# Create two variables, a and b.
# Each variable's value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 6
b = 10
if a > b:
    print("Hello World")
else:
    print("a is smaller than b")

# ===== Exercise_7.py =====
# Exercise 7: Odd or Even
# Write code that asks the user for a number
# and determines whether this number is odd or even.

number = int(input("Please write a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# ===== Exercise_8.py =====
# Exercise 8: What's your name?
# Write code that asks the user for their name
# and determines whether or not you have the same name.
# Print out a funny message based on the outcome.

user_name = input("What is your name?: ")
if user_name =="Simon":
    print ("You are also Garfunkel")
else:
    print("too bad your name is not so cool")

# ===== Exercise_9.py =====
# Exercise 9: Tall enough to ride a roller coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input("What is your height in cm? "))
if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")

