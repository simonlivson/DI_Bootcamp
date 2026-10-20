# ===== TimeChallenge2.py =====
# Time Challenge #2: Perfect number
#
# What you learn here:
#   - input() and int() type conversion
#   - for loop with range()
#   - The % (modulo) operator to find divisors
#   - Comparing values (==) to get True / False
#
# Instructions:
#   A perfect number is a positive integer that is equal to the sum of its
#   divisors. However, the number itself is not included in the sum.
#   Ask the user for a number and print whether or not it is a perfect
#   number. If yes, print True else False.
#   Hint: Google perfect numbers
#
# Example:
#   Input -- Enter the number:6
#   Output -- True
#
#   Input -- Enter the number:10
#   Output -- False
#
#   You have 30 minutes to finish this challenge.
#
# Starter code:
#   x = int(input('Enter the Number:'))
#   #write down your logic here

x = int(input('Enter the Number:'))

# ===== Way 1: Loop =====
divisors_sum = 0
for i in range(1, x):
    if x % i == 0:
        divisors_sum += i
print(divisors_sum == x)

# ===== Way 2: Comprehension with sum =====
divisors_sum2 = sum([i for i in range(1, x) if x % i == 0])
print(divisors_sum2 == x)
