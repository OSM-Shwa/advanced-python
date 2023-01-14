# Used for brute force testing until the code breaks

import random
import string


def generate_random_str(len: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    result_string = "".join(random.choice(characters) for _ in range(len))
    return result_string

if __name__ == "__main__":
    