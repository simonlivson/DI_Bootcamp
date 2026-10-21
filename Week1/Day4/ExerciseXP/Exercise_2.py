# 🌟 Exercise 2: What's Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.
#
# Key Python Topics:
# - Functions with parameters
# - String concatenation or f-strings
# - Calling functions with arguments
#
# Step 1: Define a Function with a Parameter
# - Define a function named favorite_book().
# - This function should accept one parameter called title.
#
# Step 2: Print a Message with the Title
# - The function needs to output a message like "One of my favorite books is <title>".
#
# Step 3: Call the Function with an Argument
# - Call the favorite_book() function and provide a book title as an argument.
# - For example: favorite_book("Alice in Wonderland").

# What you learn here:
# - a function with one parameter (title)
# - parameter (title, in the def) vs argument ("Alice in Wonderland", in the call)
# - return: the sentence comes back, we print it at the call
# - early-return safety check that returns a message string
# - keyword argument in the call (title = "...")
# - Way 2: the older way, a function that only prints

# ===== Way 1: return + keyword argument =====
def favorite_book(title):
# title is the parameter
    if title == "":
    # safety check: did we get a title?
        return "Please give a book title"
        # stop here and send back a message
    return f"One of my favorite books is {title}"
    # send the sentence back


print(favorite_book("Alice in Wonderland"))
# positional argument: One of my favorite books is Alice in Wonderland
print(favorite_book(title = "The Hobbit"))
# keyword argument: One of my favorite books is The Hobbit
print(favorite_book(""))
# Please give a book title


# ===== Way 2: print inside the function =====
def favorite_book_print(title):
# same parameter
    print(f"One of my favorite books is {title}")
    # print the sentence itself


favorite_book_print("Alice in Wonderland")
# One of my favorite books is Alice in Wonderland
