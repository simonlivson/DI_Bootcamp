# ===== Exercise_2.py =====
# Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to it.

my_tuple = (1, 2, 3)
# my_tuple.append(4)                # AttributeError: tuples have no append
# my_tuple[0] = 10                  # TypeError: tuples are immutable
my_tuple2 = (4, 5)
my_tuple = my_tuple + my_tuple2     # not a change, a NEW tuple with the same name
print(my_tuple)                     # (1, 2, 3, 4, 5)