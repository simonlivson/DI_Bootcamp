# ===== Exercise_5.py =====
# Exercise 5: For Loop
# Print all numbers from 1 to 20, inclusive.
# Then print every number from 1 to 20 whose index is even.

for elem in range(1, 21):
    print(elem)
numbers = list(range(1, 21))
for i in range(len(numbers)):
    if i % 2 == 0:                  # the index is even
        print(numbers[i])           # 1, 3, 5 ... 19