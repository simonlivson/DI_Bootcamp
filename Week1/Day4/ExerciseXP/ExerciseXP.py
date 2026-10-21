# ==================== Exercise_1 ====================
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


# ==================== Exercise_2 ====================
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


# ==================== Exercise_3 ====================
# 🌟 Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.
#
# Key Python Topics:
# - Functions with multiple parameters
# - Default parameter values
# - String formatting
#
# Step 1: Define a Function with Parameters
# - Define a function named describe_city().
# - This function should accept two parameters: city and country.
# - Give the country parameter a default value, such as "Unknown".
#
# Step 2: Print a Message
# - Inside the function, set up the code to display a sentence like "<city> is in <country>".
# - Replace <city> and <country> with the parameter values.
#
# Step 3: Call the Function
# - Call the describe_city() function with different city and country combinations.
# - Try calling it with and without providing the country argument to see the default value in action.
# - Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
#
# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.

# What you learn here:
# - a function with two parameters
# - a default value (country = "Unknown") used when no argument is given
# - keyword arguments in the call (city = "...", country = "...") in any order
# - return: the sentence comes back, we print it at the call
# - Way 2: the older way, a function that only prints

# ===== Way 1: return + default value + keyword arguments =====
def describe_city(city, country = "Unknown"):
# country has a default value
    return f"{city} is in {country}."
    # send the sentence back


print(describe_city("Reykjavik", "Iceland"))
# Reykjavik is in Iceland.
print(describe_city("Paris"))
# no country given -> default: Paris is in Unknown.
print(describe_city(country = "Israel", city = "Tel Aviv"))
# keyword arguments, order doesn't matter: Tel Aviv is in Israel.


# ===== Way 2: print inside the function =====
def describe_city_print(city, country = "Unknown"):
# same parameters
    print(f"{city} is in {country}.")
    # print the sentence itself


describe_city_print("Reykjavik", "Iceland")
# Reykjavik is in Iceland.
describe_city_print("Paris")
# Paris is in Unknown.


# ==================== Exercise_4 ====================
# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.
#
# Key Python Topics:
# - random module
# - random.randint() function
# - Conditional statements (if, else)
#
# Step 1: Import the random Module
# - At the beginning of your script, use import random to access the random number generation functions.
#
# Step 2: Define a Function with a Parameter
# - Create a function that accepts a number between 1 and 100 as a parameter.
#
# Step 3: Generate a Random Number
# - Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
#
# Step 4: Compare the Numbers
# - If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
#
# Step 5: Call the Function
# - Call the function with a number between 1 and 100.
#
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

# What you learn here:
# - import random
# - random.randint(low, high) gives a whole number from low to high
# - default parameters (low = 1, high = 100)
# - early-return safety check that returns a message string
# - plain if / return instead of if / else
# - return the message, then print it at the call
# - Way 2: the older way, if / else that prints

import random
# bring in the random module


# ===== Way 1: default values + early return =====
def compare_numbers(my_number, low = 1, high = 100):
# my_number is the user's guess, low and high have default values
    if my_number < low or my_number > high:
    # safety check: is the number outside the allowed range?
        return f"Number must be between {low} and {high}"
        # stop here and send back a message
    random_number = random.randint(low, high)
    # pick a random whole number between low and high
    if my_number == random_number:
    # did the guess match?
        return "Success!"
        # stop here and send back the success message
    return f"Fail! Your number: {my_number}, Random number: {random_number}"
    # we only get here when they did not match


print(compare_numbers(50))
# Success! or Fail! Your number: 50, Random number: ...
print(compare_numbers(150))
# Number must be between 1 and 100
print(compare_numbers(my_number = 5, low = 1, high = 10))
# keyword arguments: a smaller range, 1 to 10


# ===== Way 2: if / else with print =====
def compare_numbers_print(my_number):
# only the number, no defaults
    random_number = random.randint(1, 100)
    # pick a random whole number between 1 and 100
    if my_number == random_number:
    # did the guess match?
        print("Success!")
        # print success
    else:
    # they did not match
        print(f"Fail! Your number: {my_number}, Random number: {random_number}")
        # print fail and both numbers


compare_numbers_print(50)
# Success! or Fail! ...


# ==================== Exercise_5 ====================
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


# ==================== Exercise_6 ====================
# 🌟 Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.
#
# Key Python Topics:
# - Lists
# - for loops
# - Modifying lists
# - Functions that modify data structures
#
# Step 1: Create a List of Magician Names
# - Create a list called magician_names with the given names:
#   ['Harry Houdini', 'David Blaine', 'Criss Angel']
#
# Step 2: Create a Function to Display Magicians
# - Create a function called show_magicians() that takes the magician_names list as a parameter.
# - Inside the function, iterate through the list and print each magician's name.
#
# Step 3: Create a Function to Modify the List
# - Create a function called make_great() that takes the magician_names list as a parameter.
# - Inside the function, use a for loop to iterate through the list and add "the Great"
#   before each magician's name.
#
# Step 4: Call the Functions
# - Call make_great() to modify the list.
# - Call show_magicians() to display the modified list.
#
# Expected Output:
# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great

# What you learn here:
# - passing a list to a function (parameter vs argument)
# - map + lambda to change every name in one line
# - return: the function gives back the new list
# - early-return safety check (empty list) that returns a message string
# - Way 2: the older way, for i in range(len(list)) to change the list itself

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# the list from the instructions


def show_magicians(magician_names):
# print every name in the list
    if len(magician_names) == 0:
    # safety check: is the list empty?
        print("The list is empty")
        # tell the user
        return
        # stop here
    for name in magician_names:
    # go over each name
        print(name)
        # print it


# ===== Way 1: map + lambda (returns a new list) =====
def make_great(magician_names):
# gives back a NEW list with " the Great" after every name
    if len(magician_names) == 0:
    # safety check: is the list empty?
        return "The list is empty"
        # stop here and send back a message
    return list(map(lambda name: name + " the Great", magician_names))
    # map does the lambda on every name, list() turns the result into a list


magician_names = make_great(magician_names)
# save the new list in the same variable
show_magicians(magician_names)
# Harry Houdini the Great / David Blaine the Great / Criss Angel the Great
print(make_great([]))
# The list is empty


# ===== Way 2: for loop (changes the original list) =====
def make_great_loop(magician_names):
# adds " the Great" inside the same list
    if len(magician_names) == 0:
    # safety check: is the list empty?
        return "The list is empty"
        # stop here and send back a message
    for i in range(len(magician_names)):
    # i is the position: 0, 1, 2
        magician_names[i] = magician_names[i] + " the Great"
        # replace the name at position i with the new name


names_loop = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# a fresh list, so we don't get "the Great the Great"
make_great_loop(names_loop)
# changes the list itself
show_magicians(names_loop)
# Harry Houdini the Great / David Blaine the Great / Criss Angel the Great


# ==================== Exercise_7 ====================
# 🌟 Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
#
# Key Python Topics:
# - Functions
# - Conditionals (if / elif)
# - Random numbers
# - Floating-point numbers (Bonus)
# - Handling seasons (Bonus)
#
# Step 1: Create the get_random_temp() Function
# - Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
#
# Step 2: Create the main() Function
# - Create a function called main(). Inside this function:
# - Call get_random_temp() to get a random temperature.
# - Store the temperature in a variable and print a friendly message like:
#   "The temperature right now is 32 degrees Celsius."
#
# Step 3: Provide Temperature-Based Advice
# - Inside main(), provide advice based on the temperature:
# - Below 0°C: e.g., "Brrr, that's freezing! Wear some extra layers today."
# - Between 0°C and 16°C: e.g., "Quite chilly! Don't forget your coat."
# - Between 16°C and 23°C: e.g., "Nice weather."
# - Between 24°C and 32°C: e.g., "A bit warm, stay hydrated."
# - Between 32°C and 40°C: e.g., "It's really hot! Stay cool."
#
# Step 4: Floating-Point Temperatures (Bonus)
# - Modify get_random_temp() to return a random floating-point number using random.uniform()
#   for more accurate temperature values.
#
# Step 5: Month-Based Seasons (Bonus)
# - Instead of directly generating a random temperature, ask the user for a month (1-12)
#   and determine the season using if/elif conditions.
# - Modify get_random_temp() to return temperatures specific to each season.
#
# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

# What you learn here:
# - return: a function gives a value back
# - random.randint (whole numbers) and random.uniform (decimal numbers)
# - a default parameter (temperature = "random") so main can make its own temperature or get one
# - plain if / print / return checks instead of elif / else
# - early-return safety check (month 1-12) that returns a message string
# - a dict to keep each season's temperature range
# - round(x, 1) to show one decimal
# - input() + int() to ask the user for a month

# (import random is already at the top of an earlier exercise)
# bring in the random module

SEASON_TEMPS = {"winter": (-10, 16), "spring": (10, 25), "summer": (24, 40), "autumn": (10, 28)}
# lowest and highest temperature for each season (used in Step 5)


# ===== Step 1 =====
def get_random_temp():
# gives back a random whole temperature
    return random.randint(-10, 40)
    # a whole number from -10 to 40


# ===== Step 2 + Step 3 =====
def main(temperature = "random"):
# if no temperature is given, main makes a random one
    if temperature == "random":
    # nothing was given
        temperature = get_random_temp()
        # Step 1: get a random whole temperature
    print(f"The temperature right now is {temperature} degrees Celsius.")
    # friendly message
    if temperature < 0:
    # below 0
        print("Brrr, that's freezing! Wear some extra layers today.")
        # advice
        return
        # stop here
    if temperature < 16:
    # 0 to 16 (we only get here when it is 0 or more)
        print("Quite chilly! Don't forget your coat.")
        # advice
        return
        # stop here
    if temperature < 24:
    # 16 to 23
        print("Nice weather.")
        # advice
        return
        # stop here
    if temperature < 32:
    # 24 to 32
        print("A bit warm, stay hydrated.")
        # advice
        return
        # stop here
    print("It's really hot! Stay cool.")
    # everything left is 32 to 40


main()
# random whole temperature + advice


# ===== Step 4 (Bonus) =====
def get_random_temp_float():
# gives back a random decimal temperature
    return round(random.uniform(-10, 40), 1)
    # a decimal number from -10 to 40, one decimal, e.g. 23.4


main(get_random_temp_float())
# main gets the decimal temperature and reuses its advice


# ===== Step 5 (Bonus) =====
def get_season(month):
# gives back the season name for a month
    if month < 1 or month > 12:
    # safety check: is it a real month?
        return "Month must be between 1 and 12"
        # stop here and send back a message
    if month == 12 or month <= 2:
    # 12, 1, 2
        return "winter"
        # stop here
    if month <= 5:
    # 3, 4, 5
        return "spring"
        # stop here
    if month <= 8:
    # 6, 7, 8
        return "summer"
        # stop here
    return "autumn"
    # 9, 10, 11


def get_random_temp_season(season):
# gives back a random temperature for that season
    low, high = SEASON_TEMPS[season]
    # unpack the (low, high) pair, e.g. summer -> 24, 40
    return random.randint(low, high)
    # a whole number in that season's range


def main_season():
# ask for a month, then let main show the temperature and advice
    month = int(input("Enter a month (1-12): "))
    # ask the user and turn the answer into a number
    season = get_season(month)
    # winter / spring / summer / autumn, or the message
    if season not in SEASON_TEMPS:
    # safety check: did we get the message back?
        print(season)
        # show the message
        return
        # stop here
    print(f"It is {season}.")
    # tell the user the season
    main(get_random_temp_season(season))
    # main gets the season's temperature and reuses its advice


main_season()
# run it
