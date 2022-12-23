# Python list, set and dictionary comprehensions
import math

numbers = [2 ** i for i in range(1, 6)]
print(numbers)


def list_comprehension():
    # list comprehensions
    numbers = [49, 64, 81, 100, 121]
    new_list = [math.sqrt(i) for i in numbers if i % 2 == 0]
    print(new_list)
    print(new_list)

    team1 = ["Janet", "Arya", "Mary"]
    team2 = ["Evan", "Jake", "Randy"]

    new_list = [(x, y) for x in team1 for y in team2]
    print(new_list)

    word = "programming"
    alphabets = {x for x in word}
    print(alphabets)


def dict_comprehension():
    # dictionary comprehensions
    numbers = [1, 2, 3, 4, 5]
    square_dict = {num: num ** 2 for num in numbers}
    print(square_dict)

    # using dictionary comprehensions
    old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}
    new_price = {
        key: value * 1.5 if value > 2 else value for key, value in old_price.items()
    }
    print(new_price)

    # without using dictionary comprehensions
    new_price = {}
    for key, value in old_price.items():
        if value > 2:
            new_price[key] = value * 1.5
        else:
            new_price[key] = value
    print(new_price)
