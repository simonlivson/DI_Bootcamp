# Challenges
# 1.  Insert an item at a given index in a list.
# 2.  Count the spaces in a string.
# 3.  Count upper case and lower case letters in a string.
# 4.  my_sum([1,5,4,2]) -> 12, without sum().
# 5.  find_max([0,1,3,50]) -> 50
# 6.  factorial(4) -> 24
# 7.  list_count(['a','a','t','o'],'a') -> 2, without .count().
# 8.  norm([1,2,2]) -> 3 (square root of the sum of squares).
# 9.  is_mono: True if the list is sorted up or down.
#     [7,6,5,5,2,0] True, [2,3,3,3] True, [1,2,0,4] False
# 10. Print the longest word in a list.
# 11. Split a mixed list into a list of integers and a list of strings.
# 12. is_palindrome('radar') -> True, is_palindrome('John') -> False
# 13. sum_over_k('Do or do not there is no try', 2) -> 3 (words longer than k).
# 14. dict_avg({'a':1,'b':2,'c':8,'d':1}) -> 3
# 15. common_div(10,20) -> [2,5,10]
# 16. is_prime(11) -> True
# 17. weird_print([1,2,2,3,4,5]) -> [2,4] (index and value both even).
# 18. type_count(a=1,b='string',c=1.0,d=True,e=False) -> int: 1, str: 1, float: 1, bool: 2
# 19. Your own .split(): whitespace by default, or any character given.
# 20. Password format: "mypassword" -> "**********"
#
# What you learn here:
# - conditionals
# - loops
# - functions

# ===== Exercise 1: Insert an item at an index =====

fruits = ["apple", "banana", "cherry"]
# a list to work with

fruits.insert(1, "kiwi")
# .insert(index, item) puts "kiwi" at position 1 and pushes the rest to the right

print(fruits)
# ['apple', 'kiwi', 'banana', 'cherry']


# ===== Exercise 2: Count the spaces =====

text = "Do or do not there is no try"
# a string to check

spaces = 0
# the counter starts at 0

for char in text:
# go over each character

    if char == " ":
    # is it a space?

        spaces += 1
        # yes: add 1

print(spaces)
# 7


# ===== Exercise 3: Upper and lower case letters =====

text = "Hello World PYTHON"
# a string to check

upper = 0
# counter for upper case letters

lower = 0
# counter for lower case letters

for char in text:
# go over each character

    if char.isupper():
    # .isupper() is True for A-Z

        upper += 1
        # count it as upper

    if char.islower():
    # .islower() is True for a-z (spaces are neither, so they are not counted)

        lower += 1
        # count it as lower

print(f"Upper: {upper}, Lower: {lower}")
# Upper: 8, Lower: 8


# ===== Exercise 4: Sum without sum() =====

def my_sum(numbers):
# adds all the numbers in the list

    total = 0
    # start at 0

    for n in numbers:
    # go over each number

        total += n
        # add it to the total

    return total
    # give back the total

print(my_sum([1, 5, 4, 2]))
# 12


# ===== Exercise 5: Find the max =====

def find_max(numbers):
# returns the biggest number in the list

    biggest = numbers[0]
    # start by guessing the first number is the biggest

    for n in numbers[1:]:
    # check the rest of the numbers

        if n > biggest:
        # found a bigger one?

            biggest = n
            # it becomes the new biggest

    return biggest
    # give back the biggest

print(find_max([0, 1, 3, 50]))
# 50


# ===== Exercise 6: Factorial =====

def factorial(n):
# returns 1 * 2 * 3 * ... * n

    result = 1
    # start at 1 (multiplying by 0 would always give 0)

    for i in range(1, n + 1):
    # i goes 1, 2, 3, ..., n

        result *= i
        # multiply the result by i

    return result
    # give back the result

print(factorial(4))
# 24 (1 * 2 * 3 * 4)


# ===== Exercise 7: Count without .count() =====

def list_count(items, element):
# counts how many times element is in items

    count = 0
    # the counter starts at 0

    for item in items:
    # go over each item

        if item == element:
        # is it the one we are looking for?

            count += 1
            # yes: add 1

    return count
    # give back the count

print(list_count(['a', 'a', 't', 'o'], 'a'))
# 2


# ===== Exercise 8: L2-norm =====

def norm(numbers):
# square root of the sum of the squares

    squares = map(lambda n: n * n, numbers)
    # map squares every number: 1, 4, 4

    return sum(squares) ** 0.5
    # add them (9), then ** 0.5 is the square root (3.0)

print(norm([1, 2, 2]))
# 3.0


# ===== Exercise 9: Is the list monotonic? =====

def is_mono(numbers):
# True if the list is sorted up or down

    if numbers == sorted(numbers):
    # sorted() gives the list from small to big; same as ours = going up

        return True
        # it is going up

    if numbers == sorted(numbers, reverse=True):
    # reverse=True sorts from big to small; same as ours = going down

        return True
        # it is going down

    return False
    # neither up nor down

print(is_mono([7, 6, 5, 5, 2, 0]))
# True

print(is_mono([2, 3, 3, 3]))
# True

print(is_mono([1, 2, 0, 4]))
# False


# ===== Exercise 10: Longest word in a list =====

def longest(words):
# prints the longest word

    longest_word = ""
    # the longest so far; empty at the start

    for word in words:
    # go over each word

        if len(word) > len(longest_word):
        # is this word longer?

            longest_word = word
            # it becomes the new longest

    print(longest_word)
    # print it (the exercise says print, not return)

longest(["cat", "elephant", "dog"])
# elephant


# ===== Exercise 11: Split integers and strings =====

mixed = [1, "a", 2, "b", 3]
# a list with numbers and strings

integers = list(filter(lambda x: type(x) == int, mixed))
# filter keeps only the items whose type is int

strings = list(filter(lambda x: type(x) == str, mixed))
# filter keeps only the items whose type is str

print(integers)
# [1, 2, 3]

print(strings)
# ['a', 'b']


# ===== Exercise 12: Palindrome =====

def is_palindrome(word):
# True if the word reads the same backwards

    return word == word[::-1]
    # [::-1] reverses the string; compare it to the original

print(is_palindrome('radar'))
# True

print(is_palindrome('John'))
# False


# ===== Exercise 13: Words longer than k =====

def sum_over_k(sentence, k):
# counts the words that have more than k letters

    long_words = filter(lambda word: len(word) > k, sentence.split())
    # split into words, then filter keeps only words longer than k

    return len(list(long_words))
    # turn into a list and count them

print(sum_over_k('Do or do not there is no try', 2))
# 3 (not, there, try)


# ===== Exercise 14: Average of a dictionary =====

def dict_avg(d):
# returns the average of the values

    return sum(d.values()) / len(d)
    # add all the values, divide by how many there are

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
# 3.0 (12 / 4)


# ===== Exercise 15: Common divisors =====

def common_div(a, b):
# returns the numbers (above 1) that divide both a and b

    return list(filter(lambda n: a % n == 0 and b % n == 0, range(2, a + 1)))
    # try every n from 2 to a; keep it if it divides both with no remainder

print(common_div(10, 20))
# [2, 5, 10]


# ===== Exercise 16: Is it prime? =====

def is_prime(n):
# True if n can only be divided by 1 and itself

    if n < 2:
    # safety check: 0 and 1 are not prime

        return False
        # stop here

    for i in range(2, n):
    # try every number between 2 and n - 1

        if n % i == 0:
        # it divides n with no remainder

            return False
            # so n is not prime

    return True
    # nothing divided it, so it is prime

print(is_prime(11))
# True


# ===== Exercise 17: Even index and even value =====

def weird_print(numbers):
# prints the items where the index and the value are both even

    result = []
    # the matching items go here

    for i in range(len(numbers)):
    # i is the index: 0, 1, 2, ...

        if i % 2 == 0 and numbers[i] % 2 == 0:
        # the index is even and the value is even

            result.append(numbers[i])
            # keep the value

    print(result)
    # print the list

weird_print([1, 2, 2, 3, 4, 5])
# [2, 4]


# ===== Exercise 18: Count the types =====

def type_count(**kwargs):
# **kwargs collects any named arguments into a dictionary

    counts = {}
    # type name -> how many

    for value in kwargs.values():
    # go over each value we were given

        name = type(value).__name__
        # the type's name as text: "int", "str", "float", "bool"

        counts[name] = counts.get(name, 0) + 1
        # .get gives 0 the first time, then we add 1

    return counts
    # give back the dictionary

print(type_count(a=1, b='string', c=1.0, d=True, e=False))
# {'int': 1, 'str': 1, 'float': 1, 'bool': 2}


# ===== Exercise 19: Our own .split() =====

def my_split(text, separator = " "):
# splits text at separator; the default separator is a space

    parts = []
    # the finished pieces go here

    current = ""
    # the piece we are building right now

    for char in text:
    # go over each character

        if char == separator:
        # we reached a separator

            parts.append(current)
            # save the piece we built

            current = ""
            # start a new, empty piece

            continue
            # go to the next character

        current += char
        # not a separator: add the character to the piece

    parts.append(current)
    # save the last piece (there is no separator after it)

    return parts
    # give back the list

print(my_split("Do or do not"))
# ['Do', 'or', 'do', 'not']

print(my_split("a,b,c", ","))
# ['a', 'b', 'c']


# ===== Exercise 20: Password format =====

password = "mypassword"
# the password to hide

print("*" * len(password))
# a string times a number repeats it: one star for every letter

