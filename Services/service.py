from flask_restful import Resource, reqparse
import sys
sys.path.append('../')
from Data.EmployeeData import EmployeeData

employees_collection_name = "Employees"
librarians_collection_name = "Librarians"

employee_put_args =  reqparse.RequestParser()
employee_put_args.add_argument("id",type = int, help="id of the employee", required = True, location='form') 
employee_put_args.add_argument("name", help="name of the employee", required = True,location='form')
employee_put_args.add_argument("age",type = int, help="age of the employee", required = True, location='form')
employee_put_args.add_argument("yearsOfExperience",type = int, help="years of experience of the employee", location='form')




class employee(Resource):
    employee_data = EmployeeData()
    def get(self, employee_id):
        self.employee_data.abort_if_id_isnt_valid(employee_id, employees_collection_name, True)
        return self.employee_data.get_employee(employee_id)
        
    def delete(self, employee_id):
        self.employee_data.abort_if_id_isnt_valid(employee_id, employees_collection_name, True)
        return self.employee_data.delete_employee(employee_id), 202


class employees(Resource):
    employee_data = EmployeeData()

    def get(self):
        return self.employee_data.get_employees()

    def post(self, is_super = False, args = None):
            if is_super is False:
                args = employee_put_args.parse_args()

            self.employee_data.abort_if_id_isnt_valid(args.id, employees_collection_name, False) # Data layer
            
            args.isFired = False
            del args['yearsOfExperience']
            self.employee_data.post_employees(args) # Data layer

            del args['_id']
            return args, 201


class librarians(Resource):
    employee_data = EmployeeData()
    employees = employees() 

    def post(self):

        args = employee_put_args.parse_args()

        new_args = {'id': args.id, 'yearsOfExperience': args.yearsOfExperience}
        
        self.employees.post(True, args)

        self.employee_data.post_librarian(new_args)
        del new_args['_id']

        return new_args, 201