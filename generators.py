import random


def our_generator(mode: int):
    try:
        int(round(mode))
    except ValueError:
        mode = 1
    except TypeError:
        mode = 1

    # Providing all values from 1-10
    if mode == 1:
        for i in range(1, 11):
            yield i

    # Creating a fibonacci sequence
    if mode == 2:

        a = 0
        b = 1

        yield a
        yield b

        for i in range(1, 10):
            if a < b:
                a += b
                yield a
            else:
                b += a
                yield b

    # Creates a random list of incremental numbers
    if mode == 3:
        c = 1
        yield c

        for i in range(1, 101):
            d = random.randint(1, 100001)
            if d > c:
                c = d
                yield c


print(list(our_generator(2)))


def generator():
    while True:
        yield random.randint(1, 101)


# for value in generator():
#     print(value)
#     if value == 50:
#         break
