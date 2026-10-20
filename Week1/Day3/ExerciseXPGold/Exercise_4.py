# ===== Exercise_4.py =====
# Exercise 4: Fruit Shop
#
# What you learn here:
#   - Looping through a dictionary with .items()
#   - Nested dictionaries (a dictionary inside a dictionary)
#   - Calculations (price * stock) and adding up a total
#
# Instructions:
#   items = {
#       "banana": 4,
#       "apple": 2,
#       "orange": 1.5,
#       "pear": 3
#   }
#   1. Using the dictionary above, each key-value pair represents an item and
#      its price - print all the items and their prices in a sentence.
#   2. Using the dictionary below, each value are dictionaries containing both
#      the price and the amount of items in stock - write some code to
#      calculate how much it would cost to buy everything in stock.
#   items = {
#       "banana": {"price": 4 , "stock":10},
#       "apple": {"price": 2, "stock":5},
#       "orange": {"price": 1.5 , "stock":24},
#       "pear": {"price": 3 , "stock":1}
#   }

# Part 1: print all items and their prices
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for (item, price) in items.items():
    print(f"A {item} costs ${price}.")

# Part 2: cost of buying everything in stock
items2 = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for (item, info) in items2.items():
    total_cost += info["price"] * info["stock"]
print(f"Buying everything in stock costs ${total_cost}.")
