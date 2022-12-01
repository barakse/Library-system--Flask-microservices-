import string
from datetime import date

class Book:
    def __init__(self, id:int, title: string, dateAdded: date, LibrarianID : int ) -> None:
        self.id = id
        self.title = title
        self.dateAdded = dateAdded
        self.LibrarianID  = LibrarianID 

'''
book_validator = {
      "bsonType": "object",
      "required": [ "id", "name","age"],
      "properties": 
  

        "dateAdded": {
          "bsonType": "date",
          "description": "dateAdded - Required."
        },
        "LibrarianID": {
            "bsonType": "int",
          "description": "LibrarianID - Required."
        }
       }
    }
'''

book_validator = {
    "$jsonSchema":{
        "bsonType": "object",
        "required" : ["id", "name", "title", "dateAdded", "LibrarianID"],
        "properties": 
        {
          "id": {
            "bsonType": "int",
            "description": "ID - Required."
          },
          "title": {
            "bsonType": "string",
            "description": "title - Required."
          },
          "dateAdded": {
            "bsonType": "date",
            "description": "dateAdded - Required."
          },
          "LibrarianID": {
            "bsonType": "int",
            "description": "LibrarianID - Required."
          },
        }
      }
}
