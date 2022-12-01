
import string


class Employee:
    def __init__(self, id:int, name: string, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.is_fired = False

employee_validator = {
    "$jsonSchema":{
        "bsonType": "object",
        "required" : ["id", "name", "age", "isFired"],
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
          "isFired": {
              "bsonType": "bool",
              "description": "type - Required."
          },
        }
      }
}

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
 