# What we will learn:
# - Functions
#
# Exercise 2 : From English to Morse
# Instructions:
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and
# every word is separated with a slash /.

# What you learn here:
# - map + filter + lambda to translate in one line (Way 1, the main solution)
# - return + early-return safety check (empty text) that returns a message string
# - .get(key, default) so an unknown code doesn't crash
# - a dictionary as a translation table, .upper(), split() / " ".join()
# - Way 2: the older way, nested for loops

MORSE_TABLE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}
# letter -> morse code

REVERSE_TABLE = {}
# morse code -> letter (filled below)
for letter, code in MORSE_TABLE.items():
# go over every pair in the table
    REVERSE_TABLE[code] = letter
    # flip it: the code becomes the key


# ===== Way 1: map + filter + lambda =====
def english_to_morse(text):
# English -> morse in one line per word
    if text.strip() == "":
    # safety check
        return "No text given"
        # stop here and send back a message
    return " / ".join(map(lambda word: " ".join(map(lambda letter: MORSE_TABLE[letter], filter(lambda letter: letter in MORSE_TABLE, word))), text.upper().split()))
    # filter keeps known letters, inner map turns each into code, outer map does every word


def morse_to_english(morse):
# morse -> English with map
    if morse.strip() == "":
    # safety check
        return "No morse given"
        # stop here and send back a message
    return " ".join(map(lambda word: "".join(map(lambda code: REVERSE_TABLE.get(code, "?"), word.split())), morse.split("/")))
    # inner map turns each code into a letter, outer map does every word


morse = english_to_morse("Hello World")
# translate to morse
print(morse)
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_english(morse))
# HELLO WORLD
print(english_to_morse(""))
# No text given


# ===== Way 2: for loops =====
def english_to_morse_loop(text):
# English -> morse
    if text.strip() == "":
    # safety check: is there any text?
        return "No text given"
        # stop here and send back a message
    morse_words = []
    # one item per word
    for word in text.upper().split():
    # "HELLO", "WORLD"
        morse_letters = []
        # one item per letter
        for letter in word:
        # "H", "E", ...
            if letter in MORSE_TABLE:
            # skip signs we don't know
                morse_letters.append(MORSE_TABLE[letter])
                # add the code of that letter
        morse_words.append(" ".join(morse_letters))
        # letters separated by a space
    return " / ".join(morse_words)
    # words separated by a slash


def morse_to_english_loop(morse):
# morse -> English
    if morse.strip() == "":
    # safety check: is there any morse?
        return "No morse given"
        # stop here and send back a message
    english_words = []
    # one item per word
    for word in morse.split("/"):
    # every word is between slashes
        english_word = ""
        # build the word letter by letter
        for code in word.split():
        # every code is between spaces
            english_word += REVERSE_TABLE.get(code, "?")
            # unknown code -> "?" instead of a crash
        english_words.append(english_word)
        # save the word
    return " ".join(english_words)
    # words separated by a space


morse = english_to_morse_loop("Hello World")
# translate to morse
print(morse)
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_english_loop(morse))
# HELLO WORLD
print(english_to_morse_loop(""))
# No text given
