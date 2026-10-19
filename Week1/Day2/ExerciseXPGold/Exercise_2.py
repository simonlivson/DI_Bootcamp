# Exercise 2: Range of numbers
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        print(number)           # 1505, 1540, 1575 ... 2485
