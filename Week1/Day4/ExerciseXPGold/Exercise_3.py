# What we will learn:
# - Functions
#
# Exercise 3 : Double Dice
# Instructions:
# 1. Create a function that will simulate the rolling of a dice. Call it throw_dice.
#    It should return an integer between 1 and 6.
# 2. Create a function called throw_until_doubles.
#    1. It should keep throwing 2 dice (using your throw_dice function) until they both land on the
#       same number, ie. until we reach doubles.
#       For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
#    2. This function should return the number of times it threw the dice in total.
#       In the example above, it should return 3.
# 3. Create a main function.
#    It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times),
#    and store the results of those function calls (in other words, how many throws it took until
#    doubles were thrown, each time) in a collection. (What kind of collection? Read below to
#    understand what we will need the data for, and this should help you decide which data
#    structure to use).
# 4. After the 100 doubles are thrown, print out a message telling the user how many throws it took
#    in total to reach 100 doubles.
# 5. Also print out a message telling the user the average amount of throws it took to reach doubles.
#    Round this off to 2 decimal places.
# 6. For example:
#    If the results of the throws were as follows (your code would do 100 doubles, not just 3):
#    1. (1, 2), (3, 1), (5, 5)
#    2. (3, 3)
#    3. (2, 4), (1, 2), (3, 4), (2, 2)
#    Then my output would show something like this:
#    Total throws: 8
#    Average throws to reach doubles: 2.67.

# What you learn here:
# - random.randint(1, sides) for a dice, with a default parameter (sides = 6)
# - while loop that stops when a condition is met (doubles)
# - counter += 1
# - a list as the collection, then sum() / len() for the average
# - default parameter (times = 100) + early-return safety check with a message
# - round(x, 2)

import random
# bring in the random module


def throw_dice(sides = 6):
# one dice throw, 6 sides unless told otherwise
    return random.randint(1, sides)
    # a whole number from 1 to sides


def throw_until_doubles():
# keep throwing 2 dice until they match, give back how many throws it took
    count = 0
    # no throws yet
    while True:
    # keep going until we return
        dice1 = throw_dice()
        # first dice
        dice2 = throw_dice()
        # second dice
        count += 1
        # one more throw
        if dice1 == dice2:
        # doubles?
            return count
            # stop and send back the number of throws


def main(times = 100):
# throw doubles "times" times and give back the summary
    if times < 1:
    # safety check: we need at least 1 round
        return "We need at least 1 round"
        # stop here and send back a message
    results = []
    # the collection: one number per round
    for i in range(times):
    # repeat "times" times
        results.append(throw_until_doubles())
        # save how many throws this round took
    total_throws = sum(results)
    # add all the rounds together
    average = round(total_throws / len(results), 2)
    # average with 2 decimals
    return f"Total throws: {total_throws}\nAverage throws to reach doubles: {average}"
    # send back both lines


print(main())
# Total throws: ... / Average throws to reach doubles: ...
print(main(0))
# We need at least 1 round
