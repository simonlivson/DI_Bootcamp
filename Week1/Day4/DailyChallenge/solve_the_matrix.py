# Daily challenge gold: solve the matrix
#
# Goal: Decrypt a hidden message from a matrix string by processing it column-wise and filtering characters.
#
# What You'll learn
# - Python Basics
# - Conditionals
# - Loops
# - Functions
# - Lists (2D lists/matrices)
# - String Manipulation
#
# Key Python Topics:
# - Strings
# - Lists (2D lists)
# - Loops (for loops)
# - Conditional statements (if, else)
# - String methods (.isalpha(), etc.)
# - String concatenation.
#
# Instructions:
# You are given a "Matrix" string:
#
# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM#
# $a
# #t%'''
#
# This represents a grid of characters, and your task is to decode the hidden message within.
#
# Understanding the Matrix:
# - Imagine this string arranged in rows and columns, forming a grid.
# - To work with it in Python, you'll need to transform this string into a 2D list (a list of lists),
#   where each inner list represents a row.
#
# Step 1: Transforming the String into a 2D List
#
# Step 2: Processing Columns
# - Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# - You'll need to write code that iterates through the columns of your 2D list.
# - Think about how you can access the elements of a 2D list by column.
#
# Step 3: Filtering Alpha Characters
# - only select alpha characters (letters).
# - For each character in a column, check if it's an alpha character.
# - If it is, add it to a temporary string.
# - Think about how you can check if a character is an alphabet letter.
#
# Step 4: Replacing Symbols with Spaces
# - Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# - After you have gathered the alpha characters, you will need to iterate through them, and where there
#   are non alpha characters between them, you will insert a space.
# - Think about how you can keep track of when you encounter an alphabet character, and when you
#   encounter a non alphabet character.
#
# Step 5: Constructing the Secret Message
# - Combine the filtered and processed characters to form the decoded message.
# - Print the decoded message.

# What you learn here:
# - small functions with return and an early-return safety check that returns a message
# - filter + lambda to drop empty lines, map + lambda to turn every line into a list
# - map + lambda to read the 2D list column by column: matrix[row][col]
# - map + lambda + split / join to keep letters and make each symbol group ONE space
# - .isalpha() to keep only letters
# - Way 2: the older way, nested for loops and a "flag" variable (found_symbol)

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''
# the matrix from the instructions


# Step 1: Convert matrix_string to a 2D list (matrix)
def make_matrix(matrix_str):
# string -> list of rows, every row a list of characters
    if matrix_str.strip() == "":
    # safety check: is there anything to read?
        return "The matrix is empty"
        # stop here and send back a message
    lines = filter(lambda line: line != "", matrix_str.split("\n"))
    # cut into lines and drop the empty ones
    return list(map(lambda line: list(line), lines))
    # every line becomes a list of characters


# Step 2: Iterate through columns (top to bottom, left to right)
# ===== Way 1: map + lambda =====
def read_columns(matrix):
# 2D list -> one string, read column by column
    if len(matrix) == 0:
    # safety check: no rows
        return ""
        # stop here, nothing to read
    columns = map(lambda col: "".join(map(lambda row: row[col] if col < len(row) else "", matrix)), range(len(matrix[0])))
    # for every column: take that character from every row ("" when the row is too short)
    return "".join(columns)
    # glue all the columns together


# ===== Way 2: nested for loops =====
def read_columns_loop(matrix):
# 2D list -> one string, read column by column
    if len(matrix) == 0:
    # safety check: no rows
        return ""
        # stop here, nothing to read
    column_text = ""
    # we add characters here
    for col in range(len(matrix[0])):
    # every column, left to right
        for row in range(len(matrix)):
        # every row, top to bottom
            if col < len(matrix[row]):
            # some rows are shorter, skip missing spots
                column_text += matrix[row][col]
                # add the character
    return column_text
    # send the text back


# Step 3 + 4: keep letters, one space for each group of symbols between two letters
# ===== Way 1: map + lambda + split / join =====
def decode(column_text):
# every symbol -> space, then split() + join() makes each group ONE space
    if column_text == "":
    # safety check
        return "Nothing to decode"
        # stop here and send back a message
    spaced = "".join(map(lambda char: char if char.isalpha() else " ", column_text))
    # letters stay, symbols become spaces
    return " ".join(spaced.split())
    # split() drops all the extra spaces, join puts one space back


# ===== Way 2: flag variable =====
def decode_loop(column_text):
# keep letters, one space for every group of symbols between two letters
    if column_text == "":
    # safety check
        return "Nothing to decode"
        # stop here and send back a message
    decoded_message = ""
    # the answer
    found_symbol = False
    # did we just see symbols?
    for char in column_text:
    # every character
        if not char.isalpha():
        # a symbol
            found_symbol = True
            # remember it
            continue
            # go to the next character
        if found_symbol and decoded_message != "":
        # symbols came between two letters
            decoded_message += " "
            # one space for the whole group
        decoded_message += char
        # add the letter
        found_symbol = False
        # reset the flag
    return decoded_message
    # send the message back


# Step 5: Print the decoded message
matrix = make_matrix(MATRIX_STR)
# Step 1
column_text = read_columns(matrix)
# Step 2, Way 1
print(decode(column_text))
# Way 1: This is Matrix
print(decode_loop(read_columns_loop(matrix)))
# Way 2: This is Matrix
