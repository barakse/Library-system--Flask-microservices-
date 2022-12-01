from pymongo import MongoClient
from Models.Employee import employee_validator
from Models.Librarian import librarian_validator
from Models.Book import book_validator
cluster = "mongodb+srv://barakse222:123MongoDB@library-flask.censagw.mongodb.net/Library-Flask?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(cluster)

db = client["Library-Flask"]

names_in_collections = db.list_collection_names()
names_to_add_collections = ["Librarians","Employees","Books"]

def buildCollection(name, validator_checker):
    if name not in db.list_collection_names():
        db.create_collection(name)
    
    db.command("collMod", name, validator=validator_checker)
try:
    active = False
    if active:
        buildCollection("Librarians", librarian_validator)
        buildCollection("Employees", employee_validator)
        buildCollection("Books", book_validator)
except Exception as e:
    print(e)
