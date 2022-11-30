from flask_restful import reqparse
from dbConnection import db
#from Models.Librarian import validator
#from Models.Employee import employee_validator
#from Models.Librarian import librarian_validator
#from Models.Book import book_validator

employee_put_args =  reqparse.RequestParser()
employee_put_args.add_argument("id",type = int, help="id of the employee", required = True, location='form') 
employee_put_args.add_argument("name", help="name of the employee", required = True,location='form')
employee_put_args.add_argument("age",type = int, help="age of the employee", required = True, location='form')
employee_put_args.add_argument("yearsOfExperience",type = int, help="years of experience of the employee", location='form')

#db.runCommand( { collMod: "Employees",validator={
 #   validator})
 
def buildCollection(name):
    if name not in db.list_collection_names():
        db.create_collection(name)
    
    #db.command("collMod", name, validator=validatork)
try:
    buildCollection("Employees")
    print(db.list_collection_names())
except:
    print("FAILED")
#buildCollection("Librarians", librarian_validator)
#buildCollection("Books", book_validator)