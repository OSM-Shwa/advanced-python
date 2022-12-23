from contextlib import contextmanager


class Open_File:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# with Open_File("sample.txt", "w") as f:
#     f.write("Testing")

# print(f.closed)


# #### Using contextlib ####


@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    yield f
    f.close()


with open_file("sample.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")

print(f.closed)
