
import string
from datetime import date


class Book:
    def __init__(self, id:int, title: string, dateAdded: date, LibrarianID : int ) -> None:
        self.id = id
        self.title = title
        self.dateAdded = dateAdded
        self.LibrarianID  = LibrarianID 

 