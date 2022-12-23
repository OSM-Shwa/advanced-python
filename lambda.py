import random

"""# def double(n):
#     return n*2

double = lambda n: n * 2

print(double(10))

larger = lambda a, b: a if a > b else b
print(larger(10, 47))

names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]


def len_of_names(n):
    return len(n)


names.sort(key=lambda x: len(x))
print(names)

"""

# using a def function
def chance_of_rain(a, b):
    return (a + b) % 2 == 0


# print(chance_of_rain(10, 3))

# using a lambda function
COR = lambda a, b: (a + b) % 2 == 0
# print(COR(10, 4))

# 1-liner
# you can set default values too! (make sure you always
# have the second pair of brackets even if you dont pass any arguments)
# print((lambda a=2, b=10: (a + b) % 2 == 0)())

# passing functions as arguments
def rand():
    return random.randint(1, 101)


# print((lambda a, b: (a + b) % 2 == 0)(100, rand()))
# order of and: false then true
# print((lambda a, b: (a + b) % 2 and "odd" or "even")(100, rand()))

# using map and filter with lambda functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 21, 23, 25, 27, 29]
nums2 = list(map(lambda x: x + 5, numbers))
print(nums2)

nums3 = list(filter((lambda x: x % 2 == 0), numbers))
print(nums3)
