# Strings: ordered, immutable, text representation


def tip1():
    my_string = "Hello World"
    substring = my_string[1:5]
    print(substring)


def tip2():
    greeting = "Hello"
    name = "Joshua"
    sentence = greeting + name
    print(sentence)


def tip3():
    greeting = "Hello"
    for i in greeting:
        print(i)


def tip4():
    my_string = "how are you doing"
    my_list = my_string.split()
    new_string = " ".join(my_list)
    print(new_string)


def tip5():
    my_list = ["a"] * 6
    # bad python code
    my_string = ""
    for i in my_list:
        my_string += i

    # good python code
    my_string = "".join(my_list)
    return my_string


def string_formatting():

    # method 1: %s (string)
    var = "Joshua"
    my_string = "the variable is %s" % var
    print(my_string)

    # method 1: %d (integers)
    var = 3
    my_string = "the variable is %d" % var
    print(my_string)

    # method 1: %f (floats)
    var = 3.14159
    my_string = "the variable is %.2f" % var
    print(my_string)

    # method 2: .format() method
    var = 3.14159
    my_string = "the variable is {:.2f}".format(var)
    print(my_string)

    # method 3: f-strings
    var = 3.14159
    my_string = f"the variable is {var:.2f}"
    print(my_string)


string_formatting()
