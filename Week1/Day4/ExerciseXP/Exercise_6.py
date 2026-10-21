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
