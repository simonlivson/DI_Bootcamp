# ===== Exercise_4.py =====
# Exercise 4: Floats
# A float is a number with a decimal point (2.5), an integer is a whole number (2).
# Create the list 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without typing each number.

numbers = []
for elem in range(3, 11):           # 3, 4, 5 ... 10
    if elem % 2 == 0:
        numbers.append(elem // 2)   # even: whole result, stays an integer (2, 3, 4, 5)
    else:
        numbers.append(elem / 2)    # odd: result is a float (1.5, 2.5, 3.5, 4.5)
print(numbers)                      # [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
