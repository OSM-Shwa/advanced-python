
from getpass import getpass

def ternary_statement(condition):

    x = 1 if condition else 0
    print(x)


def context_manager():
    # pythonic way:
    with open("text.txt", "r") as f:
        file_contents = f.read()

    words = file_contents.split(" ")
    word_count = len(words)
    print(word_count)


def use_enumerate():
    names = ["Corey", "Chris", "Dave", "Travis"]
    for index, name in enumerate(names, start=1):
        print(index, name)


def heroes():
    names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
    heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
    universes = ["Marvel", "DC", "Marvel", "DC"]
    # works but not pythonic
    """for index, name in enumerate(names):
        hero = heroes[index]
        print(f"{name} is actually {hero}!")
    """
    # the pythonic way
    for name, hero, universe in zip(names, heroes, universes):
        print(f"{name} is actually {hero} from {universe}!")


def password():
    username = input("Username: ")
    password = getpass("Password: ")
    
    print("Logging in...")
    return username, password

password()