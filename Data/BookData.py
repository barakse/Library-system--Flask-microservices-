from dbConnection import db
from flask_restful import abort

db_Employees = db.get_collection("Employees")
db_Librarians = db.get_collection("Librarians")
db_Books = db.get_collection("Books")

class BookData:
    def abort_if_id_isnt_valid(self,id, db_collection, is_exist):
        if ((db[db_collection].find_one({"id": id}) is None) == is_exist):
            if(is_exist):
               abort(404, message="This ID dosent exist in " + db_collection)
            
            else:
                abort(409, message="This ID already exist in " + db_collection) 
    
    def abort_if_librarian_isnt_valid(self,LibrarianID):
        if (db_Librarians.find_one({"id":int(LibrarianID)}) is not None):
            if db_Employees.find_one({"id":LibrarianID,"isFired": True}):
               abort(408, message="This employee is fired!")
        else:
            abort(404, message="Sorry! librarian dosent exists")

    def get_book(self, id): #get DONE
        return db_Books.find_one({'id': id}, {'_id':0})

    def put_book(self,id,args):
        db_Books.find_one_and_update({"id":id}, {"$set":args},{'_id':0})

    def delete_book(self,id):
        return db_Books.find_one_and_delete({'id':id},{'_id':0})
    
    def get_books(self):
        books_dict = list(db_Books.find({}, {'_id': False}))
        return books_dict[0] if len(books_dict) == 1 else books_dict
    
    def insert_book(self, args):
        db_Books.insert_one(args)