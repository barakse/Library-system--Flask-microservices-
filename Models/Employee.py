
import string


class Employee:
    def __init__(self, id:int, name: string, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.is_fired = False

 