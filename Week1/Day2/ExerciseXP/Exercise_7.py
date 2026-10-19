# ===== Exercise_7.py =====
# Exercise 7: Favorite Fruits
# Ask for favorite fruits separated by spaces, store them in a list.
# Ask for any fruit and say whether it is one of the favorites.

fav_fruits = input("Enter your favorite fruits, separated by spaces: ").split()
fruit = input("Enter the name of any fruit: ")
if fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")