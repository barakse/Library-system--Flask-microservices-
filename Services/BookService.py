from flask_restful import  Resource, abort, reqparse
from BookData import book_put_args
from dbConnection import db
from datetime import date

book_put_args =  reqparse.RequestParser()
book_put_args.add_argument("id",type= int, help="id of the employee", required = True, location='form') 
book_put_args.add_argument("title", help="name of the employee", required = True,location='form')
book_put_args.add_argument("dateAdded",type = date.fromisoformat, help="dateAdded of the employee", required = True, location='form')
book_put_args.add_argument("LibrarianID",type= int, help="age of the employee", required = True, location='form')


db_books = db.get_collection("Books")
db_Librarians = db.get_collection("Librarians")
db_employees = db.get_collection("Employees")

def abort_if_book_id_dosent_exist(book_id):
    if (db_books.find_one({"id":book_id}) is None):
        abort(404, message="There isnt a book with this ID...")

def abort_if_book_exists(book_id):
    if (db_books.find_one({"id":book_id}) is not None):
        abort(409, message="book already exists with that ID...")

def abort_if_librarian_isnt_valid(LibrarianID):
    print(LibrarianID)

    
    if (db_Librarians.find_one({"id":int(LibrarianID)}) is not None):
        if db_employees.find_one({"id":LibrarianID,"isFired": True}):
            abort(408, message="This employee is fired!")
    else:
        abort(404, message="Sorry! librarian dosent exists")

class book(Resource):
    def get(self, book_id): #get DONE
        abort_if_book_id_dosent_exist(book_id)
        books_dict = db_books.find_one({'id': book_id}, {'_id':0})
        return books_dict

    def put(self, book_id):
        abort_if_book_id_dosent_exist(book_id)
        args = book_put_args.parse_args()
        if args.id != book_id:
            abort(409, message="book id(key) dosent match to values id")
            
        abort_if_librarian_isnt_valid(args.LibrarianID)

        args.dateAdded = date.isoformat(args.dateAdded)
        item = db_books.find_one_and_update({"id":book_id}, {"$set":args},{'_id':0})
        
        return item, 201

    def delete(self, book_id):
        abort_if_book_id_dosent_exist(book_id)
        item = db_books.find_one_and_delete({'id':book_id},{'_id':0})
        return item,202

class books(Resource):
    def get(self):
        books_dict = list(db_books.find({}, {'_id': False}))
        return books_dict[0] if len(books_dict) == 1 else books_dict

    def post(self):
        args = book_put_args.parse_args()
        args.dateAdded = date.isoformat(args.dateAdded)

        abort_if_book_exists(args.id)
        abort_if_librarian_isnt_valid(args.LibrarianID)
        db_books.insert_one(args)
        del args['_id']
       
        return args, 201
    


