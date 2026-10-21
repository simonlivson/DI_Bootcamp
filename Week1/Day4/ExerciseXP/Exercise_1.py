# 🌟 Exercise 1: What Are You Learning?
# Goal: Create a function that displays a message about what you're learning.
#
# Key Python Topics:
# - Functions (defining and calling)
# - print() function
#
# Step 1: Define a Function
# - Define a function named display_message().
# - This function should not take any parameters.
#
# Step 2: Print a Message
# - For example: "I am learning about functions in Python."
#
# Step 3: Call the Function
# - This will execute the code inside the function and print your message.
#
# Expected Output:
# I am learning about functions in Python.

# What you learn here:
# - def: how to define a function
# - return: the function gives the message back, we print it at the call
# - a default value (message = "...") so the function also works with no argument
# - keyword argument in the call (message = "...")
# - Way 2: the older way, a function that only prints

# ===== Way 1: return + default value =====
def display_message(message = "I am learning about functions in Python."):
# message has a default value, so we can call it with no argument
    return message
    # send the message back


print(display_message())
# I am learning about functions in Python.
print(display_message(message = "I am learning about lambda in Python."))
# keyword argument: I am learning about lambda in Python.


# ===== Way 2: print inside the function (no parameters) =====
def display_message_print():
# no parameters, exactly like Step 1
    print("I am learning about functions in Python.")
    # print the message itself


display_message_print()
# I am learning about functions in Python.
