# example 1
numbers = list(range(100))

# correct but not pythonic
squares = []
for number in numbers:
    if number % 5 == 0:
        squares.append(number ** 2)

# better way to do it
squares = [number ** 2 for number in numbers if number % 5 == 0]
# print(squares)


# creating a filtered list, but in the bad way
filtered_list = []
for x in numbers:
    if x % 5 == 0 and x % 3 == 0:
        squares.append(x)

filtered_list = list(filter(lambda x: x % 5 == 0 and x % 3 == 0, numbers))
# print(filtered_list)

# https://www.youtube.com/watch?v=PDqy1HoA3QM&t=689s


# bad coding
ridiculous_words = [
    "Everywhen",
    "Hullaballoo",
    "Sozzled",
    "Titter",
    "Smicker",
    "Foppish",
    "Schmooze",
    "Smaze",
]
words_without_e = []

for word in ridiculous_words:
    if "e" not in word:
        words_without_e.append(word)

# using list comprehension
words_without_e = [word+"text" for word in ridiculous_words if "e" not in word]
print(words_without_e)

# using the map function to add a word to the end of each list item
def add_word(word: str):
    return word + "text"


new_words = list(map(add_word, ridiculous_words))
print(new_words)
