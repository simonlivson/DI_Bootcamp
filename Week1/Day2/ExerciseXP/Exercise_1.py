# ===== Exercise_1.py =====
# Exercise 1: Favorite Numbers
# Create a set called my_fav_numbers with your favorite numbers.
# Add two new numbers, then remove the last one you added.
# Create friend_fav_numbers, then combine both into our_fav_numbers.

my_fav_numbers = {7, 13, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(100)
my_fav_numbers.remove(100)          # remove the last number added
print(my_fav_numbers)
friend_fav_numbers = {3, 7, 50}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)              # 7 appears only once, sets have no duplicates
