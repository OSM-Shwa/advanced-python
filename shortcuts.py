# 10 useful shortcuts in python


def shortcut1():
    # f-strings
    name = "Tim"
    print(f"Hello {name} {2+3}")


def shortcut2():
    # unpacking
    tup = (1, 2, 3, 4, 5)
    list = [1, 2, 3, 4, 5]
    str = "Hello"
    dict = {"a": 1, "b": 2}
    coords = [4, 5]

    x, y = coords
    print(x, y)


def shortcut3():
    # multiple assignment
    height, width = 400, 500

    # bad
    temp = height
    height = width
    height = temp

    # good
    height, width = width, height
    print(height, width)


def shortcut4():
    # comprehensions

    # good
    x = [i for i in range(100) if i % 2 == 0]
    z = [[0 for _ in range(5)] for _ in range(5)]
    a = (i for i in "hello")
    print(list(a))

    sentence = "hello my name is Joshua"
    b = {char: sentence.count(char) for char in set(sentence)}
    print(b)

    # bad
    y = []
    for _ in range(100):
        y.append(0)

    return x, z


def shortcut5():
    # object mulitplication
    my_list = [[1, 2]] * 5


def shortcut6():
    # inline / ternary conditions
    x = 1 if 2 > 3 else 0
    print(x)


def shortcut7():
    names = ["tim", "joe", "billy", "sally"]
    ages = [21, 19, 18, 43]
    eye_colors = ["blue", "brown", "brown", "green"]

    print(list(zip(names, ages, eye_colors)))

    for name, age, eye_color in zip(names, ages, eye_colors):
        if age > 20:
            print(name)
            print(eye_color)


# *args and **kwargs
def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


# args: order/position in which you pass the args MATTERS,
# you have to pass the args to avoid an error
args = [1, 2, 3]

# kwargs: order/position in which you pass the kwargs DOES NOT MATTER,
# you do not have to pass the kwargs
kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}

# func1(*args)
# func2(**kwargs)


def shortcut9():
    # for else and while else
    search = [1, 2, 3, 4, 5, 6, 7]
    target = 8

    for element in search:
        if element == target:
            print("I found it!")
            break
    else:
        print("I didn't find it!")

    i = 0
    while i < len(search):
        element = search[i]
        if element == target:
            print("I found it!")
            break
        i += 1
    else:
        print("I didn't find it!")


def shortcut10():
    # sort by key

    def sort_func(x):
        return x[0] + x[1]

    list = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
    list.sort(key=sort_func)  # key=lambda x: x[1]
    print(list)

# https://www.youtube.com/watch?v=CssrFJGH_dU
