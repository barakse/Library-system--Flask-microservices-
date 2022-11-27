from flask_restful import reqparse


employee_put_args =  reqparse.RequestParser()
employee_put_args.add_argument("id", help="id of the employee", required = True, location='form') 
employee_put_args.add_argument("name", help="name of the employee", required = True,location='form')
employee_put_args.add_argument("age", help="age of the employee", required = True, location='form')
'''
librarian_put_args = reqparse.RequestParser()
librarian_put_args.add_argument("id", help="id of the employee", required = True, location='form') 
librarian_put_args.add_argument("name", help="name of the employee", required = True,location='form')
librarian_put_args.add_argument("age", help="age of the employee", required = True, location='form')

'''
employee_put_args.add_argument("yearsOfExperience", help="years of experience of the employee", location='form')




