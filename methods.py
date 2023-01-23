from typing import Self
from datetime import date


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def description(self) -> str:
        return f'{self.name} is {self.age} years old.'
    
    @classmethod
    def age_from_year(cls, name: str, birth_year: int) -> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)
        

class Calculator:
    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f"Currently running Calculator on version: {self.version}")

    @staticmethod
    def add_numbers(self, *numbers: float) -> float:
        return sum(numbers)


if __name__ == "__main__":
    federico = Person.age_from_year("Federico", 1997)
    print(federico.description())