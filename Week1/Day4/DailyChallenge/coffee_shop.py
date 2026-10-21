# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.
#
# Write a program that:
# 1. Stores the coffee shop menu in memory
# 2. Lets the user:
#    - Create a new item
#    - Read (view) all items
#    - Update an item's price
#    - Delete an item
#    - Exit
# Your program must be organized with functions. Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.
#
# 1. Data structure:
# We will represent the menu using a dictionary called menu.
# The key is the drink name (string). The value is the price (float).
# Example starting data (you MUST start with this so tests are consistent):
# menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}
#
# 2. Required functions:
# a) show_menu(menu_dict)
#    Input: the dictionary. Output: prints all items in the format drink - price₪.
#    If the menu is empty, print: "The menu is empty."
#    Example:
#    Current menu:
#    espresso - 7.0₪
#    latte - 12.0₪
#    cappuccino - 10.0₪
#    This function only prints. It does not return anything.
# b) add_item(menu_dict)
#    Ask the user for: drink name, price. Add it to the dictionary.
#    If the drink already exists, print "Item already exists!" and do not change the price.
#    Example interaction:
#    Enter new drink name: mocha
#    Enter price: 14
#    "mocha" added!
#    This function mutates the dictionary. It does not return anything.
# c) update_price(menu_dict)
#    Ask the user which drink they want to update.
#    If it exists: ask for the new price, update it, print: "Price updated!"
#    If it doesn't exist: print: "Item not found."
# d) delete_item(menu_dict)
#    Ask the user which drink to remove.
#    If it exists: delete it from the dict, print: "Item deleted."
#    Otherwise: print: "Item not found."
# e) show_options()
#    Prints the main menu of actions for the user:
#    What would you like to do?
#    1. Show menu
#    2. Add item
#    3. Update price
#    4. Delete item
#    5. Exit
#    Only prints. Doesn't return anything.
# f) run_coffee_shop()
#    This is the main controller of the program.
#    Behavior: Keep running in a loop. Show options. Ask the user to choose (1-5).
#    Depending on the choice, call the correct function.
#    Rules: Invalid choice → print "Invalid choice, try again."
#           Choice 5 stops the loop and prints "Goodbye!"
#
# 3. Program flow example:
#    prompts use '> ' for the choice; 'Which drink do you want to update? ', 'Enter the new price: ',
#    'Which drink do you want to delete? ', blank line between rounds.
#
# 4. Starter template:
#    menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}
#    def show_menu(menu_dict): """Print all drinks and prices."""
#    def add_item(menu_dict): """Add a new drink to the menu."""
#    def update_price(menu_dict): """Change the price of an existing drink."""
#    def delete_item(menu_dict): """Remove a drink from the menu."""
#    def show_options(): """Print the available actions."""
#    def run_coffee_shop():
#        """Main loop of the program."""
#        # TODO:
#        # while True:
#        #   1. show_options()
#        #   2. get user choice
#        #   3. if 1 -> show_menu(menu)
#        #      if 2 -> add_item(menu)
#        #      if 3 -> update_price(menu)
#        #      if 4 -> delete_item(menu)
#        #      if 5 -> print("Goodbye!") and break
#        #      else -> "Invalid choice, try again."
#    # Start the program
#    run_coffee_shop()
#
# 5. Extra challenges (only if they finish early):
# 1. Validation: Don't allow negative prices. If the user enters -5, print "Invalid price."
#    and don't change anything.
# 2. Search function: Add a function search_item(menu_dict) that asks for a drink name and:
#    prints the price if found, else prints "Not in the menu." Then add it as option 6 in the menu.
# 3. Discount day: Add a function apply_discount(menu_dict, percent) that reduces every price
#    by a percentage. Example: apply_discount(menu, 10) makes 10% off happy hour.
#    (Added as option 7 so it can be run.)

# What you learn here:
# - splitting a program into small functions, each with early-return safety checks
#   (plain if / print / return instead of if / else)
# - a default parameter (percent = 10)
# - filter + lambda: search by part of the name (Way 1 of search)
# - map + lambda + zip: discount every price (Way 1 of discount)
# - reduce + lambda and sum(): total menu value (option 8)
# - return values (is_valid_price, total value, handle_choice)
# - CRUD with a dictionary, "key in dict", del dict[key] (earlier material)
# - Way 2 versions: the older for loop ways
# - checking a price with .replace(".", "", 1).isdigit() before float()
# - while True + break as the main loop

from functools import reduce
# bring in reduce from the functools module

menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}
# the starting menu from the instructions


def is_valid_price(text):
# True if the text is a positive number like "14" or "12.5"
    return text.replace(".", "", 1).isdigit()
    # remove one dot, then only digits may be left ("-5" fails because of "-")


def show_menu(menu_dict):
    """Print all drinks and prices."""
    if len(menu_dict) == 0:
    # safety check: is the menu empty?
        print("The menu is empty.")
        # tell the user
        return
        # stop here
    print("Current menu:")
    # title
    for drink, price in menu_dict.items():
    # go over every drink and its price
        print(f"{drink} - {price}₪")
        # espresso - 7.0₪


def add_item(menu_dict):
    """Add a new drink to the menu."""
    name = input("Enter new drink name: ")
    # ask for the name
    if name in menu_dict:
    # safety check: does it already exist?
        print("Item already exists!")
        # tell the user
        return
        # stop here, don't change the price
    price = input("Enter price: ")
    # ask for the price (still text)
    if not is_valid_price(price):
    # Extra 1: safety check, no negative or wrong prices
        print("Invalid price.")
        # tell the user
        return
        # stop here
    menu_dict[name] = float(price)
    # add the new drink
    print(f'"{name}" added!')
    # confirm


def update_price(menu_dict):
    """Change the price of an existing drink."""
    name = input("Which drink do you want to update? ")
    # ask which drink
    if name not in menu_dict:
    # safety check: does it exist?
        print("Item not found.")
        # tell the user
        return
        # stop here
    new_price = input("Enter the new price: ")
    # ask for the new price
    if not is_valid_price(new_price):
    # Extra 1: safety check
        print("Invalid price.")
        # tell the user
        return
        # stop here
    menu_dict[name] = float(new_price)
    # save the new price
    print("Price updated!")
    # confirm


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    name = input("Which drink do you want to delete? ")
    # ask which drink
    if name not in menu_dict:
    # safety check: does it exist?
        print("Item not found.")
        # tell the user
        return
        # stop here
    del menu_dict[name]
    # remove it
    print("Item deleted.")
    # confirm


# Extra 2: search
# ===== Way 1: filter + lambda (part of the name is enough) =====
def search_item(menu_dict):
    """Print every drink whose name contains what the user typed."""
    name = input("Which drink are you looking for? ")
    # e.g. "lat" finds latte
    matches = list(filter(lambda drink: name.lower() in drink.lower(), menu_dict))
    # keep only the drink names that contain the typed text
    if len(matches) == 0:
    # safety check: nothing found?
        print("Not in the menu.")
        # tell the user
        return
        # stop here
    for drink in matches:
    # every drink that matched
        print(f"{drink} - {menu_dict[drink]}₪")
        # show its price


# ===== Way 2: exact name with "in" =====
def search_item_loop(menu_dict):
    """Print the price of one drink."""
    name = input("Which drink are you looking for? ")
    # ask which drink
    if name not in menu_dict:
    # safety check: is it on the menu?
        print("Not in the menu.")
        # tell the user
        return
        # stop here
    print(f"{name} - {menu_dict[name]}₪")
    # show its price


# Extra 3: discount
# ===== Way 1: map + lambda =====
def apply_discount(menu_dict, percent = 10):
    """Reduce every price by a percentage (10% unless told otherwise)."""
    if percent <= 0 or percent >= 100:
    # safety check: the percent must be between 0 and 100
        print("Discount must be between 0 and 100.")
        # tell the user
        return
        # stop here
    new_prices = list(map(lambda price: round(price * (100 - percent) / 100, 2), menu_dict.values()))
    # map does the discount on every price: 7.0 -> 6.3
    for drink, new_price in zip(list(menu_dict), new_prices):
    # zip pairs every drink name with its new price
        menu_dict[drink] = new_price
        # save the new price
    print(f"{percent}% discount applied!")
    # confirm


# ===== Way 2: for loop =====
def apply_discount_loop(menu_dict, percent = 10):
    """Reduce every price by a percentage (10% unless told otherwise)."""
    if percent <= 0 or percent >= 100:
    # safety check: the percent must be between 0 and 100
        print("Discount must be between 0 and 100.")
        # tell the user
        return
        # stop here
    for drink in menu_dict:
    # go over every drink
        menu_dict[drink] = round(menu_dict[drink] * (100 - percent) / 100, 2)
        # 10% off: price * 90 / 100
    print(f"{percent}% discount applied!")
    # confirm


# Extra (option 8): total value of the menu
# ===== Way 1: reduce + lambda =====
def total_value_reduce(menu_dict):
    """Give back the sum of all prices."""
    if len(menu_dict) == 0:
    # safety check: is the menu empty?
        return "The menu is empty."
        # stop here and send back a message
    return reduce(lambda result, e: result + e, menu_dict.values())
    # 7.0 + 12.0 = 19.0, 19.0 + 10.0 = 29.0


# ===== Way 2: sum() =====
def total_value_sum(menu_dict):
    """Give back the sum of all prices."""
    if len(menu_dict) == 0:
    # safety check: is the menu empty?
        return "The menu is empty."
        # stop here and send back a message
    return sum(menu_dict.values())
    # the built-in sum adds all the prices


def show_options():
    """Print the available actions."""
    print("What would you like to do?")
    # title
    print("1. Show menu")
    # option 1
    print("2. Add item")
    # option 2
    print("3. Update price")
    # option 3
    print("4. Delete item")
    # option 4
    print("5. Exit")
    # option 5
    print("6. Search item")
    # option 6 (Extra 2)
    print("7. Apply discount")
    # option 7 (Extra 3)
    print("8. Show total menu value")
    # option 8 (extra)


def handle_choice(choice):
    """Run the action for one choice. Returns False only when the user wants to exit."""
    if choice == "1":
    # show menu
        show_menu(menu)
        # call the function
        return True
        # keep going
    if choice == "2":
    # add item
        add_item(menu)
        # call the function
        return True
        # keep going
    if choice == "3":
    # update price
        update_price(menu)
        # call the function
        return True
        # keep going
    if choice == "4":
    # delete item
        delete_item(menu)
        # call the function
        return True
        # keep going
    if choice == "5":
    # exit
        print("Goodbye!")
        # say bye
        return False
        # stop the loop
    if choice == "6":
    # search
        search_item(menu)
        # Way 1: filter + lambda (search_item_loop is Way 2)
        return True
        # keep going
    if choice == "7":
    # discount
        percent = input("Enter discount percent (Enter = 10): ")
        # ask for the percent, empty means the default
        if percent == "":
        # nothing typed
            apply_discount(menu)
            # Way 1 with the default 10% (apply_discount_loop is Way 2)
            return True
            # keep going
        if not is_valid_price(percent):
        # safety check: must be a number
            print("Invalid percent.")
            # tell the user
            return True
            # keep going
        apply_discount(menu, float(percent))
        # Way 1 with the typed percent
        return True
        # keep going
    if choice == "8":
    # total menu value
        print(f"Total menu value (reduce): {total_value_reduce(menu)}")
        # Way 1
        print(f"Total menu value (sum): {total_value_sum(menu)}")
        # Way 2
        return True
        # keep going
    print("Invalid choice, try again.")
    # anything else is not allowed
    return True
    # keep going


def run_coffee_shop():
    """Main loop of the program."""
    while True:
    # keep running until the user exits
        show_options()
        # print the actions
        choice = input("> ")
        # ask for a choice
        if not handle_choice(choice):
        # handle_choice gave back False -> the user chose 5
            break
            # leave the loop
        print()
        # blank line between rounds


# Start the program
run_coffee_shop()
# run it
