from flask_restful import reqparse
from datetime import date
book_put_args =  reqparse.RequestParser()
book_put_args.add_argument("id",type= int, help="id of the employee", required = True, location='form') 
book_put_args.add_argument("title", help="name of the employee", required = True,location='form')
book_put_args.add_argument("dateAdded",type = date.fromisoformat, help="dateAdded of the employee", required = True, location='form')
book_put_args.add_argument("LibrarianID",type= int, help="age of the employee", required = True, location='form')

