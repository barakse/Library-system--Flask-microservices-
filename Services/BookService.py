#from ..Controllers import EmployeeController
from flask_restful import Api, Resource, reqparse, abort
from BookData import book_put_args
import json


def abort_if_book_id_dosent_exist(book_id):
    #print(empolyees_dict)
    s = str(book_id)
    with open('./DB/books_dict.json', 'r') as openfile:
            books_dict = json.load(openfile)
        
    if s not in books_dict:
        abort(404, message="couldnt find, isnt VALID...")

def abort_if_book_exists(book_id):
    with open('./DB/books_dict.json', 'r') as openfile:
        books_dict = json.load(openfile)
    if book_id in books_dict:
        abort(409, message="empolyee already exists with that ID...")

def abort_if_librarian_isnt_valid_exist(LibrarianID):
    #print(empolyees_dict)
    s = str(LibrarianID)
    with open('./DB/librarian_dict.json', 'r') as openfile:
        librarian_dict = json.load(openfile)
    if s not in librarian_dict:
        abort(404, message="couldnt find, isnt VALID...")
    else:
        print(librarian_dict[s])
        if librarian_dict[s]['isFired']:
            abort(404, message="Sorry! librarian isnt working here anymore...")

class book(Resource):
    def get(self, book_id):
        print("book get")
        abort_if_book_id_dosent_exist(book_id)
        with open('../DB/books_dict.json', 'r') as openfile:
            books_dict = json.load(openfile)
        return books_dict[str(book_id)]

    def put(self, book_id):
        abort_if_book_id_dosent_exist(book_id)
        with open('./DB/books_dict.json','r') as f:
                books_dict = json.load(f)

        args = book_put_args.parse_args()
        if args.id != str(book_id):
            abort(409, message="book id(key) dosent match to values id")
            
        books_dict[args.id] = args

        with open('./DB/books_dict.json','w') as f:
            json.dump(books_dict,f)
        
        print("Hey sugar")
        return books_dict[args.id], 201

    def delete(self, book_id):
        abort_if_book_id_dosent_exist(book_id)
        with open('./DB/books_dict.json','r') as f:
            books_dict = json.load(f)

        item_removed = books_dict[str(book_id)]
        del books_dict[str(book_id)]

        with open('./DB/books_dict.json','w') as f:
            json.dump(books_dict,f)
     
        return item_removed,202

class books(Resource):

    def get(self):
        print("Reg-books get")
        with open('../DB/books_dict.json', 'r') as openfile:
            books_dict = json.load(openfile)
        return books_dict

    def post(self):
        args = book_put_args.parse_args()
  
        abort_if_librarian_isnt_valid_exist(args.LibrarianID)
        abort_if_book_exists(args.id)

        with open('./DB/books_dict.json','r') as f:
            books_dict = json.load(f)

        books_dict.update({args.id:args})

        with open('./DB/books_dict.json','w') as f:
            json.dump(books_dict,f)
       
        print("Hey sugar")
        return books_dict[args.id], 201
    


