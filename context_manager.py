# Context Manager in Python


class File:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Opening {self.name}...")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"Closing {self.name}...")


if __name__ == "__main__":
    with File("main.py") as file:
        print(file.name)

    print("Done!")


f = open("sample.txt", "w")
f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
f.close

# with open("sample.txt", "w") as f:
#     f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
