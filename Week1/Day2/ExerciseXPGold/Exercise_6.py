# Exercise 6: Words and letters
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence
# of the letter variable in each word of the list.
# If the letter doesn't exist in one of the words, print a friendly message
# with the word and the letter.

words = []
for i in range(7):
    words.append(input(f"Enter word {i + 1}: "))

letter = input("Enter a single letter: ")

for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"'{letter}' first appears in '{word}' at index {index}")
    else:
        print(f"Sorry, the letter '{letter}' is not in '{word}'")
