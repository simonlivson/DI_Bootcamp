# What we will learn:
# - Functions
#
# Exercise 1 : What's your name ?
# Instructions:
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it's omitted by the user, the name returned should only contain
# the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

# What you learn here:
# - optional parameter with a default value ("")
# - keyword arguments
# - .capitalize() to make the first letter big
# - early-return safety check that returns a message string
# - plain if / return instead of if / else
# - Way 2: *names + map + lambda to capitalize any amount of names

# ===== Way 1: default value + keyword arguments =====
def get_full_name(first_name, last_name, middle_name = ""):
# middle_name is optional: "" when it is not given
    if first_name == "" or last_name == "":
    # safety check: first and last name are required
        return "First and last name are required"
        # stop here and send back a message
    if middle_name == "":
    # no middle name given
        return f"{first_name.capitalize()} {last_name.capitalize()}"
        # stop here: Bruce Lee
    return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    # we only get here when there is a middle name: John Hooker Lee


print(get_full_name(first_name = "john", middle_name = "hooker", last_name = "lee"))
# John Hooker Lee
print(get_full_name(first_name = "bruce", last_name = "lee"))
# Bruce Lee
print(get_full_name(first_name = "", last_name = "lee"))
# First and last name are required


# ===== Way 2: *names + map + lambda =====
def get_full_name_args(*names):
# names collects all the given names into a tuple, in order
    if len(names) < 2:
    # safety check: we need at least a first and a last name
        return "We need at least a first and a last name"
        # stop here and send back a message
    return " ".join(map(lambda name: name.capitalize(), names))
    # capitalize every name, then glue them with spaces


print(get_full_name_args("john", "hooker", "lee"))
# John Hooker Lee
print(get_full_name_args("bruce", "lee"))
# Bruce Lee
print(get_full_name_args("bruce"))
# We need at least a first and a last name
