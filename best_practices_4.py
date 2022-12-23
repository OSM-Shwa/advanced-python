from time import sleep


print("This is my file to demonstrate best practices.")


def process_data(data: str):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data


def read_data_from_web() -> str:
    print("Reading data from the Web")
    data = "Data from the Web"
    return data


def write_data_to_database(data: str) -> None:
    print("Writing data to the database")
    print(data)


def main() -> None:
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)


if __name__ == "__main__":
    main()
