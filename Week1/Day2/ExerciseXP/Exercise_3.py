# ===== Exercise_3.py =====
# Exercise 3: List Manipulation
# Remove "Banana" and "Blueberries", add "Kiwi" to the end,
# add "Apples" to the beginning, count "Apples", then empty the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)                       # ['Apples', 'Apples', 'Oranges', 'Kiwi']
print(basket.count("Apples"))       # 2
basket.clear()
print(basket)                       # []