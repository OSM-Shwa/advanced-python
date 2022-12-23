from pathlib import Path


def main() -> None:
    print(f"Current working directory: {Path.cwd()}")  # current working directory
    print(f"Home directory: {Path.home()}")  # home directory

    path = Path("/usr/bin/python3")  # create a path object
    path1 = Path("/usr/") / "bin" / "python3"
    
    print(path.exists())  # check if the path exists


if __name__ == "__main__":
    main()
