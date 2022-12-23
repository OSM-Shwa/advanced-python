# ? Reading a file
def read_file():
    with open("python.txt", "r") as f:
        content = f.read()
        print(content)


# ? Writing to a file
# if the file doens't exist, it will create a new file with that name
# It will override any existing content when you write to it
def write_to_file():
    with open("python.txt", "w") as f:
        f.write("Python is my favourite programming language!")


# ? Appending to a file
def append_to_file():
    with open("python.txt", "a") as f:
        f.write("\nPython is my favourite programming language!")


# ? Using the readlines() method
# returns a list with each item being a line of the file
def read_lines_of_file():
    with open("python.txt", "r") as f:
        lines = f.readlines()
        print(lines)


# ? Using the writelines() method
# writes each item of a list to the file
def write_lines_to_file():
    with open("javascript.txt", "w") as f:
        lines = [
            "JS is also awesome!",
            "\nJS is my second favourite programming language!",
        ]
        f.writelines(lines)


# write_lines_to_file()

# https://www.youtube.com/watch?v=crluPcyuchU
