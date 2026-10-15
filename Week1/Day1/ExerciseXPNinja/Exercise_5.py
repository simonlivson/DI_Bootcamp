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