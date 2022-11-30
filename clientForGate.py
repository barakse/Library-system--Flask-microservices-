import requests
from datetime import date
import json

def clearJsonFile(path):
    open(path, 'w').close()
    with open(path, "w") as outfile:
        json.dump({}, outfile)

BASE = "http://127.0.0.1:9000/"

book_data = [{"id": 4, "title": "Sulami","dateAdded": date.today(),"LibrarianID": 2},
            {"id": 2, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 5},
            {"id": 9, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 10},
            {"id": 9, "title": "Zooki","dateAdded": date.today(),"LibrarianID": 10}]

data = [{"id": 4, "name": "TheCobra", "age": 1000}, {"id": 2, "name": "Joe", "age": 78,'yearsOfExperience': 100 },
{"id": 3, "name": "Dean", "age": 26}, {"id": 2, "name": "Joe", "age": 78,'yearsOfExperience': 100 },
{"id": 10, "name": "Barak", "age": 26,'yearsOfExperience': 20 }]

#EMPLOYEE HANDLING
#response = requests.post(BASE + "employees/add", data[0])
#response = requests.post(BASE + "employees/librarian/add", data[4]) 
#response = requests.get(BASE + "employees")
#response = requests.get(BASE + "employees/2")
#response = requests.get(BASE + "employees/2")
#response = requests.delete(BASE + "employees/2")
#response = requests.get(BASE + "employees/2")

#BOOK HANDLING
response = requests.post(BASE + "books/add", book_data[3])
response = requests.put(BASE + "books/update/9", book_data[2])
#response = requests.delete(BASE + "books/9")
#response = requests.get(BASE + "books/10")
#response = requests.get(BASE + "books")

print(response.json())
