# 🌟 Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
#
# Key Python Topics:
# - Functions
# - Conditionals (if / elif)
# - Random numbers
# - Floating-point numbers (Bonus)
# - Handling seasons (Bonus)
#
# Step 1: Create the get_random_temp() Function
# - Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
#
# Step 2: Create the main() Function
# - Create a function called main(). Inside this function:
# - Call get_random_temp() to get a random temperature.
# - Store the temperature in a variable and print a friendly message like:
#   "The temperature right now is 32 degrees Celsius."
#
# Step 3: Provide Temperature-Based Advice
# - Inside main(), provide advice based on the temperature:
# - Below 0°C: e.g., "Brrr, that's freezing! Wear some extra layers today."
# - Between 0°C and 16°C: e.g., "Quite chilly! Don't forget your coat."
# - Between 16°C and 23°C: e.g., "Nice weather."
# - Between 24°C and 32°C: e.g., "A bit warm, stay hydrated."
# - Between 32°C and 40°C: e.g., "It's really hot! Stay cool."
#
# Step 4: Floating-Point Temperatures (Bonus)
# - Modify get_random_temp() to return a random floating-point number using random.uniform()
#   for more accurate temperature values.
#
# Step 5: Month-Based Seasons (Bonus)
# - Instead of directly generating a random temperature, ask the user for a month (1-12)
#   and determine the season using if/elif conditions.
# - Modify get_random_temp() to return temperatures specific to each season.
#
# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

# What you learn here:
# - return: a function gives a value back
# - random.randint (whole numbers) and random.uniform (decimal numbers)
# - a default parameter (temperature = "random") so main can make its own temperature or get one
# - plain if / print / return checks instead of elif / else
# - early-return safety check (month 1-12) that returns a message string
# - a dict to keep each season's temperature range
# - round(x, 1) to show one decimal
# - input() + int() to ask the user for a month

import random
# bring in the random module

SEASON_TEMPS = {"winter": (-10, 16), "spring": (10, 25), "summer": (24, 40), "autumn": (10, 28)}
# lowest and highest temperature for each season (used in Step 5)


# ===== Step 1 =====
def get_random_temp():
# gives back a random whole temperature
    return random.randint(-10, 40)
    # a whole number from -10 to 40


# ===== Step 2 + Step 3 =====
def main(temperature = "random"):
# if no temperature is given, main makes a random one
    if temperature == "random":
    # nothing was given
        temperature = get_random_temp()
        # Step 1: get a random whole temperature
    print(f"The temperature right now is {temperature} degrees Celsius.")
    # friendly message
    if temperature < 0:
    # below 0
        print("Brrr, that's freezing! Wear some extra layers today.")
        # advice
        return
        # stop here
    if temperature < 16:
    # 0 to 16 (we only get here when it is 0 or more)
        print("Quite chilly! Don't forget your coat.")
        # advice
        return
        # stop here
    if temperature < 24:
    # 16 to 23
        print("Nice weather.")
        # advice
        return
        # stop here
    if temperature < 32:
    # 24 to 32
        print("A bit warm, stay hydrated.")
        # advice
        return
        # stop here
    print("It's really hot! Stay cool.")
    # everything left is 32 to 40


main()
# random whole temperature + advice


# ===== Step 4 (Bonus) =====
def get_random_temp_float():
# gives back a random decimal temperature
    return round(random.uniform(-10, 40), 1)
    # a decimal number from -10 to 40, one decimal, e.g. 23.4


main(get_random_temp_float())
# main gets the decimal temperature and reuses its advice


# ===== Step 5 (Bonus) =====
def get_season(month):
# gives back the season name for a month
    if month < 1 or month > 12:
    # safety check: is it a real month?
        return "Month must be between 1 and 12"
        # stop here and send back a message
    if month == 12 or month <= 2:
    # 12, 1, 2
        return "winter"
        # stop here
    if month <= 5:
    # 3, 4, 5
        return "spring"
        # stop here
    if month <= 8:
    # 6, 7, 8
        return "summer"
        # stop here
    return "autumn"
    # 9, 10, 11


def get_random_temp_season(season):
# gives back a random temperature for that season
    low, high = SEASON_TEMPS[season]
    # unpack the (low, high) pair, e.g. summer -> 24, 40
    return random.randint(low, high)
    # a whole number in that season's range


def main_season():
# ask for a month, then let main show the temperature and advice
    month = int(input("Enter a month (1-12): "))
    # ask the user and turn the answer into a number
    season = get_season(month)
    # winter / spring / summer / autumn, or the message
    if season not in SEASON_TEMPS:
    # safety check: did we get the message back?
        print(season)
        # show the message
        return
        # stop here
    print(f"It is {season}.")
    # tell the user the season
    main(get_random_temp_season(season))
    # main gets the season's temperature and reuses its advice


main_season()
# run it
