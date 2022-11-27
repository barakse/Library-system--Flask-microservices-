import requests
from datetime import date
import json

def clearJsonFile(path):
    open(path, 'w').close()
    with open(path, "w") as outfile:
        json.dump({}, outfile)

BASE = "http://127.0.0.1:9000/"

book_data = [{"id": 1, "title": "Sulami","dateAdded": date.today(),"LibrarianID": 2},
            {"id": 2, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 5},
            {"id": 1, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 2}]

data = [{"id": 1, "name": "NumberOne", "age": 1000}, {"id": 2, "name": "Joe", "age": 78,'yearsOfExperience': 100 }]

clearJsonFile('./DB/employees_dict.json')
clearJsonFile('./DB/librarian_dict.json')
clearJsonFile('./DB/books_dict.json')

#EMPLOYEE HANDLING
response = requests.post(BASE + "employees/add", data[0])
response = requests.post(BASE + "employees/librarian/add", data[1]) 
response = requests.get(BASE + "employees")
response = requests.get(BASE + "employees/2")
response = requests.delete(BASE + "employees/1")
response = requests.get(BASE + "employees/2")

#BOOK HANDLING
response = requests.post(BASE + "books/add", book_data[0])
response = requests.put(BASE + "books/update/1", book_data[2])
response = requests.get(BASE + "books/1")
response = requests.get(BASE + "books")

print(response.json())
