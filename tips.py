## PYTHON TIPS FOR BETTER CODE ##
import sys

# ? 1) Iterate with enumerate() instead of range(len())


def tip1():
    data = [1, 2, -3, -4]
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    print(data)

    data = [1, 2, -3, -4]
    for idx, num in enumerate(data):
        if num < 0:
            data[idx] = 0
    print(data)


# ? 2) Use LIST COMPREHENSION instead of raw "for loops"
def tip2():
    squares = []
    for i in range(10):
        squares.append(i * i)
    print(squares)

    squares = [i * i for i in range(10)]
    print(squares)


# ? 3) Sort complexe iterables with sorted()
def tip3():
    data = [3, 5, 1, 10, 9]
    sorted_data = sorted(data, reverse=True)
    print(sorted_data)

    data = [
        {"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9},
    ]

    sorted_data = sorted(data, key=lambda x: x["age"])
    print(sorted_data)


# ? 4) Store unique values using SETS
def tip4():
    my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]
    my_set = set(my_list)
    print(my_set)


# ? 5) save memory with GENERATORS
def tip5():
    my_list = [i for i in range(10000)]  # this is a list
    print(sum(my_list))
    print(sys.getsizeof(my_list), "bytes")  # 85176 bytes

    my_gen = (i for i in range(10000))  # this is a set/generator
    print(sum(my_gen))
    print(sys.getsizeof(my_gen), "bytes")  # 104 bytes


# ? 6) Define default values in dictionaries with .get() and .setdefault()
def tip6():
    my_dict = {"item": "football", "price": 10.00}
    count = my_dict.get("count")
    print(count)


# https://www.youtube.com/watch?v=8OKTAedgFYg
