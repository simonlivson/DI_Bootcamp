# ===== Exercise_6.py =====
# Exercise 6: While Loop
# Ask the user for their name. Using while True, keep asking until
# the name is not digits and at least 3 letters long, then print "thank you".

while True:
    name = input("Enter your name: ")
    if name.isdigit() or len(name) < 3:
        print("Invalid name, try again")
    else:
        print("thank you")
        break
