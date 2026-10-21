# 🌟 Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.
#
# Key Python Topics:
# - Functions with multiple parameters
# - Default parameter values
# - String formatting
#
# Step 1: Define a Function with Parameters
# - Define a function named describe_city().
# - This function should accept two parameters: city and country.
# - Give the country parameter a default value, such as "Unknown".
#
# Step 2: Print a Message
# - Inside the function, set up the code to display a sentence like "<city> is in <country>".
# - Replace <city> and <country> with the parameter values.
#
# Step 3: Call the Function
# - Call the describe_city() function with different city and country combinations.
# - Try calling it with and without providing the country argument to see the default value in action.
# - Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
#
# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.

# What you learn here:
# - a function with two parameters
# - a default value (country = "Unknown") used when no argument is given
# - keyword arguments in the call (city = "...", country = "...") in any order
# - return: the sentence comes back, we print it at the call
# - Way 2: the older way, a function that only prints

# ===== Way 1: return + default value + keyword arguments =====
def describe_city(city, country = "Unknown"):
# country has a default value
    return f"{city} is in {country}."
    # send the sentence back


print(describe_city("Reykjavik", "Iceland"))
# Reykjavik is in Iceland.
print(describe_city("Paris"))
# no country given -> default: Paris is in Unknown.
print(describe_city(country = "Israel", city = "Tel Aviv"))
# keyword arguments, order doesn't matter: Tel Aviv is in Israel.


# ===== Way 2: print inside the function =====
def describe_city_print(city, country = "Unknown"):
# same parameters
    print(f"{city} is in {country}.")
    # print the sentence itself


describe_city_print("Reykjavik", "Iceland")
# Reykjavik is in Iceland.
describe_city_print("Paris")
# Paris is in Unknown.
