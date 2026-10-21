# 🌟 Exercise 5: Let's Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt's size and message, with default values.
#
# Key Python Topics:
# - Functions with parameters and default values
# - Keyword arguments
#
# Step 1: Define a Function with Parameters
# - Define a function called make_shirt().
# - This function should accept two parameters: size and text.
#
# Step 2: Print a Summary Message
# - Set up the function to display a sentence summarizing the shirt's size and message.
#
# Step 3: Call the Function
#
# Step 4: Modify the Function with Default Values
# - Modify the make_shirt() function so that size has a default value of "large"
#   and text has a default value of "I love Python".
#
# Step 5: Call the Function with Default and Custom Values
# - Call make_shirt() to make a large shirt with the default message.
# - Call make_shirt() to make a medium shirt with the default message.
# - Call make_shirt() to make a shirt of any size with a different message.
#
# Step 6 (Bonus): Keyword Arguments
# - Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).
#
# Expected Output:
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

# What you learn here:
# - default values + keyword arguments + **kwargs (the main focus)
# - return: the sentence comes back, we print it at the call
# - a function with two parameters
# - default values (used when you don't give an argument)
# - positional arguments vs keyword arguments (size="small")
# - **kwargs: extra keyword arguments arrive as a dict, read with .get(key, default)

# ===== Way 2 (Step 1-3): first version, no default values, only prints =====
def make_shirt_basic(size, text):
# size and text must both be given
    print(f"The size of the shirt is {size} and the text is {text}.")
    # print the summary sentence


make_shirt_basic("XL", "Hello World")
# The size of the shirt is XL and the text is Hello World.


# ===== Way 1 (Step 4-6): default values + return + keyword arguments =====
# Step 4: same function with default values
def make_shirt(size = "large", text = "I love Python"):
# if no size or text is given, the defaults are used
    return f"The size of the shirt is {size} and the text is {text}."
    # send the summary sentence back


# Step 5
print(make_shirt())
# large + default message
print(make_shirt("medium"))
# medium + default message
print(make_shirt("small", "Custom message"))
# any size + different message

# Step 6 (Bonus): keyword arguments
print(make_shirt(size = "small", text = "Hello!"))
# keywords say which value goes where
print(make_shirt(text = "Keyword first!", size = "medium"))
# order doesn't matter with keywords


# ===== Way 1 extra: **kwargs =====
# Extra (practice **kwargs): any extra details about the shirt
def make_shirt_extra(size = "large", text = "I love Python", **kwargs):
# kwargs collects every extra keyword argument into a dict
    color = kwargs.get("color", "white")
    # read "color" from kwargs, or use "white" if it was not given
    return f"The size of the shirt is {size}, the text is {text} and the color is {color}."
    # send the sentence back


print(make_shirt_extra())
# ... and the color is white.
print(make_shirt_extra("small", "Hi!", color = "black"))
# ... and the color is black.
