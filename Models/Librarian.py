#from . import Employee
import Employee
import string

class Librarian(Employee):

    def __init__(self, id:int, name: string, age: int,yearsOfExperience: int) -> None:
        super().__init__(id, name, age)
        self.yearsOfExperience  = yearsOfExperience
