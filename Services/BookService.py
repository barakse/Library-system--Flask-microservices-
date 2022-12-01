from flask_restful import  Resource, abort, reqparse
from dbConnection import db
from datetime import date
from Data.BookData import BookData

book_put_args =  reqparse.RequestParser()
book_put_args.add_argument("id",type= int, help="id of the employee", required = True, location='form') 
book_put_args.add_argument("title", help="name of the employee", required = True,location='form')
book_put_args.add_argument("dateAdded",type = date.fromisoformat, help="dateAdded of the employee", required = True, location='form')
book_put_args.add_argument("LibrarianID",type= int, help="age of the employee", required = True, location='form')


employees_collection_name = "Employees"
librarians_collection_name = "Librarians"
books_collection_name = "Books"

class book(Resource):
    book_data = BookData()

    def get(self, book_id): #get DONE
        self.book_data.abort_if_id_isnt_valid(book_id, books_collection_name, True)
        return self.book_data.get_book(book_id)

    def put(self, book_id):
        self.book_data.abort_if_id_isnt_valid(book_id, books_collection_name, True)
        args = book_put_args.parse_args()

        if args.id != book_id:
            abort(409, message="book id(key) dosent match to values id")
            
        self.book_data.abort_if_librarian_isnt_valid(args.LibrarianID)
        args.dateAdded = date.isoformat(args.dateAdded)
        self.book_data.put_book(book_id,args)

        return args, 201

    def delete(self, book_id):
        self.book_data.abort_if_id_isnt_valid(book_id, books_collection_name, True)
        return self.book_data.delete_book(book_id),202

class books(Resource):
    book_data = BookData()

    def get(self):
        return self.book_data.get_books()

    def post(self):
        args = book_put_args.parse_args()
        args.dateAdded = date.isoformat(args.dateAdded)

        self.book_data.abort_if_id_isnt_valid(args.id, books_collection_name, False)
        self.book_data.abort_if_librarian_isnt_valid(args.LibrarianID)
        self.book_data.insert_book(args)
        
        del args['_id']
        return args, 201
    


