from .Employee import Employee
import string

class Librarian(Employee):
    def __init__(self, id:int, name: string, age: int,yearsOfExperience: int) -> None:
        super().__init__(id, name, age)
        self.yearsOfExperience  = yearsOfExperience

librarian_validator = {
      "bsonType": "object",
      "required": [ "id", "name","age","yearsOfExperience"],
      "properties": 
      {
        "id": {
          "bsonType": "int",
          "description": "ID - Required."
        },
        "name": {
          "bsonType": "string",
          "description": "name - Required."
        },
        "age": {
          "bsonType": "int",
          "description": "age - Required."
        },
        "yearsOfExperience": {
            "bsonType": "int",
            "description": "yearsOfExperience - Required."
        },
        "isfired": {
            "bsonType": "bool"
        }
    }
}

