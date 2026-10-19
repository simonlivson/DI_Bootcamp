# ===== Exercise_8.py =====
# Exercise 8: Pizza Toppings
# Ask for toppings one by one until the user types 'quit'.
# Print "Adding [topping] to your pizza." each time.
# At the end print all toppings and the total cost ($10 base + $2.50 per topping).

toppings = []
while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping == "quit":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + 2.5 * len(toppings)
print(f"Your toppings: {', '.join(toppings)}")
print(f"Total cost: ${total_cost}")