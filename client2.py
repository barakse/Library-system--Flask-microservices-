import requests
from datetime import date
import ssl
import json
#from Data import librarian_dict, empolyees_dict
def clearJsonFile(path):
    open(path, 'w').close()
    with open(path, "w") as outfile:
        json.dump({}, outfile)

BASE = "http://127.0.0.1:5000/"
BOOKBASE= "http://127.0.0.1:8000/"

book_data = [{"id": 1, "title": "Sulami","dateAdded": date.today(),"LibrarianID": 2},
            {"id": 2, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 5},
            {"id": 1, "title": "Moshe","dateAdded": date.today(),"LibrarianID": 5}]

data = [{"id": 1, "name": "NumberOne", "age": 1000}, {"id": 2, "name": "Joe", "age": 78,'yearsOfExperience': 100 }]

#CLEAR AREA
clearJsonFile('./DB/employees_dict.json')
clearJsonFile('./DB/librarian_dict.json')
clearJsonFile('./DB/books_dict.json')

#POST EMPOLOYEE
response = requests.post(BASE + "employees/add", data[0]) 
response = requests.post(BASE + "employees/librarian/add", data[1]) 
response = requests.delete(BASE + "employees/2")
print(response.json())

#GET EMPLOYEE
response = requests.get(BASE + "employees")
response = requests.get(BASE + "employees/1")


#BOOK HANDLING
print("Moving to book")
response = requests.post(BOOKBASE + "books/add", book_data[0])
print(response.json())
response = requests.put(BOOKBASE + "books/update/1", book_data[1])
#response = requests.delete(BOOKBASE + "books/1")



'''for i, d in enumerate(data):
    response = requests.put(BASE + "video/"+ str(i), d) 
    print(response.json())
'''



