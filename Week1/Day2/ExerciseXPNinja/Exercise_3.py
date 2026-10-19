# Exercise 3: Working on a paragraph
# Paste a paragraph of text and store it in a variable.
# Print how many characters, sentences, words and unique words it contains.
# Bonus: non-whitespace characters, average words per sentence, non-unique words.

paragraph = "Python is a popular programming language. It was created by Guido van Rossum and first released in 1991. Python is known for its simple and readable code. Many people use Python for data science and artificial intelligence."

characters = len(paragraph)
sentences = paragraph.count(".")          # each sentence ends with a period
words = paragraph.split()
unique_words = set(words)
non_whitespace = len(paragraph.replace(" ", ""))
average_words = len(words) / sentences
non_unique_words = len(words) - len(unique_words)

print(f"Characters: {characters}")
print(f"Sentences: {sentences}")
print(f"Words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Non-whitespace characters: {non_whitespace}")
print(f"Average words per sentence: {average_words}")
print(f"Non-unique words: {non_unique_words}")
