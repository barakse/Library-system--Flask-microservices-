
import string


class Employee:
    def __init__(self, id:int, name: string, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.is_fired = False
'''
employee_validator = {
      "bsonType": "object",
      "requierd" : ["name"],
      "properties": 
      {
        "id": {
          "bsonType": "int",
          "description": "ID - Required."},
        "name": {
          "type": "string",
          "description": "name - Required."
        },
        "age": {
          "type": "int",
          "description": "age - Required."
        },
         "isFired": {
            "type": "boolean",
            "description": "type - Required."
       }
        "name": {
          "bsonType": "string",
          "description": "name - Required."
        }
      }
}
'''
'''       
           "id": {
          "type": "integer",
          "description": "ID - Required."},
        "name": {
          "type": "string",
          "description": "name - Required."
        },
        "age": {
          "type": "integer",
          "description": "age - Required."
        },
         "isFired": {
            "type": "boolean",
            "description": "type - Required."
       }
        }'''
 