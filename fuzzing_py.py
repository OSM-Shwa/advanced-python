# Used for brute force testing until the code breaks

import random
import string

MAX_STR_LEN = 100


def generate_random_str(len: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    result_string = "".join(random.choice(characters) for _ in range(len))
    return result_string


def fuzzer() -> str:
    while True:
        yield generate_random_str(random.randint(1, MAX_STR_LEN))


def sample_function(input_str: str) -> int:
    try:
        if "!!!" in input_str:
            raise Exception("bad input")
        return 0
    except Exception as e:
        print("Error:", e)
        return 1


def main():
    i: int = 0
    for input_str in fuzzer():
        i += 1
        result: int = sample_function(input_str)

        if result == 1:
            print(f"Run #{i} \nCause -> {input_str}")
            break


if __name__ == "__main__":
    main()
