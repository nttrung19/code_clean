#Example 5: Class with Type Hints
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1

person = Person("Alice", 30)
person.birthday()