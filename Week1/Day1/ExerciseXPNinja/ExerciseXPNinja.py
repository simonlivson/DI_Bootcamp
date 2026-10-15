# ===== Exercise_1.py =====
# Exercise 1: Use the terminal
# Run this command in the terminal to open a python console:
# $ python3
# Hint: Replace python3 with python for Windows
# Read about the PATH variable. Try to explain why you can call python3
# if you aren't in the executable directory.
# PATH explanation: https://linuxconfig.org/linux-path-environment-variable

# Answer: PATH is an environment variable that holds a list of folders.
# When I type a command like python, the system searches those folders
# for the program. Python's folder is in PATH, so I can run it from
# any directory without typing its full location.

# ===== Exercise_2.py =====
# Exercise 2: Alias
# Read about alias, and try to open a python console with the command:
# $ py

# Exercise 2: Alias
# Read about alias, and try to open a python console with the command:
# $ py

# Answer: An alias is a short nickname for a longer command.
# In the terminal I typed:
#   alias py=python
# Then typing py opened the Python console, just like typing python.
# The alias lasts until I close the terminal. To keep it for good,
# I can add it to the ~/.bashrc file.

# ===== Exercise_3.py =====
# Exercise 3: Outputs
# Predict the output of the following code snippets:

print(3 <= 3 < 9)                     # True
print(3 == 3 == 3)                    # True
print(bool(0))                        # False
print(bool(5 == "5"))                 # False
print(bool(4 == 4) == bool("4" == "4"))  # True
print(bool(bool(None)))               # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)  # x is True
print("y is", y)  # y is False
print("a:", a)    # a: 5
print("b:", b)    # b: 10

# ===== Exercise_4.py =====
# Exercise 4: How many characters in a sentence?
# Use python to find out how many characters are in the following text,
# using a single line of code (beyond the my_text variable).

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))

# ===== Exercise_5.py =====
# Exercise 5: Longest word without a specific character
# Keep asking the user to input the longest sentence they can without the character "A".
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_length = 0

while True:
    sentence = input("Write the longest sentence you can without the letter A: ")
    if "a" in sentence or "A" in sentence:
        print("Oops, your sentence has an A in it. Try again!")
    elif len(sentence) > longest_length:
        longest_length = len(sentence)
        print(f"Congratulations! New record: {longest_length} characters!")
    else:
        print(f"Good try, but the record is still {longest_length} characters.")

