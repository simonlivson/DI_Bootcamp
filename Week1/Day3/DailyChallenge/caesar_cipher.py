# ===== caesar_cipher.py =====
# Daily Challenge Gold: Caesar Cypher
#
# What you learn here:
#   - Python Basics
#   - Conditionals
#   - Loops
#   (plus ord() / chr() to turn letters into numbers and back)
#
# Instructions:
#   In cryptography, a Caesar cipher is one of the simplest and most widely
#   known encryption techniques. It is a type of substitution cipher in which
#   each letter in the plaintext is replaced by a letter some fixed number of
#   positions down the alphabet.
#
#   For example, with a left shift of 3 -> D would be replaced by A,
#   -> E would become B, and so on.
#
#   The method is named after Julius Caesar, who used it in his private
#   correspondence.
#
#   Create a python program that encrypts and decrypts messages with ceasar
#   cypher. The user enters the program, and then the program asks him if he
#   wants to encrypt or decrypt, and then execute encryption/decryption on a
#   given message and a given shift.
#
#   Check out this tutorial: https://cryptii.com/pipes/caesar-cipher
#
# Hint:
#   for letter in text:
#       cypher_text += chr(ord(letter) + 3)

choice = input("Do you want to encrypt or decrypt? ")
text = input("Enter your message: ")
shift = int(input("Enter the shift: "))

if choice == "decrypt":
    shift = -shift

cypher_text = ""
for letter in text:
    if letter.isupper():
        cypher_text += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    elif letter.islower():
        cypher_text += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    else:
        cypher_text += letter
print(cypher_text)
