from flask_restful import Api, Resource, reqparse

#new requset object- auto parse and make sure it fits to our info and grab it

#help message for error to the sender

book_put_args =  reqparse.RequestParser()
book_put_args.add_argument("id", help="id of the employee", required = True, location='form') 
book_put_args.add_argument("title", help="name of the employee", required = True,location='form')
book_put_args.add_argument("dateAdded", help="age of the employee", required = True, location='form')
book_put_args.add_argument("LibrarianID", help="age of the employee", required = True, location='form')


books_dict = {}