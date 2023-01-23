from typing import Self
from datetime import date


class Calculator:
    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f"Currently running Calculator on version: {self.version}")

    @staticmethod
    def add_numbers(self, *numbers: float) -> float:
        return sum(numbers)


if __name__ == "__main__":
    calc1 = Calculator(10)
    calc2 = Calculator(200)

    calc1.description()
    calc2.description()
    