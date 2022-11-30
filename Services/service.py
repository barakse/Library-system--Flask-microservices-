from flask_restful import Resource, abort
from Data import employee_put_args
import json
import sys
sys.path.append('../')
from dbConnection import db

db_employees = db.get_collection("Employees")
db_Librarians = db.get_collection("Librarians")


def check_if_key_in_JSON_file_dict(id,path):
    with open(path) as openJson:
        dict = json.load(openJson)
    return str(id) in dict

def abort_if_employee_id_dosent_exist(employee_id):
    if (db_employees.find_one({"id":employee_id}) is None):
        abort(404, message="There isnt an employee with this ID...")

def abort_if_empolyee_exists(employee_id):
    if (db_employees.find_one({"id":employee_id}) is not None):
        abort(409, message="empolyee already exists with that ID...")
    return 


class employee(Resource):
    def get(self, employee_id):
        abort_if_employee_id_dosent_exist(employee_id)
        empolyees_dict = db_employees.find_one({'id': employee_id}, {'_id':0})
        return empolyees_dict
        
    def delete(self, employee_id):
        abort_if_employee_id_dosent_exist(employee_id)
        item = db_employees.find_one_and_update({'id':employee_id},{"$set":{'isFired':True}},{'_id':0})

        return item,202


class employees(Resource):

    def get(self):
        empolyees_dict = list(db_employees.find({}, {'_id': False}))
        print(empolyees_dict[0] if len(empolyees_dict) == 1 else empolyees_dict)
        return empolyees_dict[0] if len(empolyees_dict) == 1 else empolyees_dict

    def post(self, is_super = False, args = None):
            if is_super is False:
                args = employee_put_args.parse_args()

            abort_if_empolyee_exists(args.id)
            args.isFired = False
            del args['yearsOfExperience']
            db.Employees.insert_one(args)

            del args['_id']
            return args, 201


class librarians(Resource):
    def post(self):
        args = employee_put_args.parse_args()
        new_args = {'id': args.id, 'yearsOfExperience': args.yearsOfExperience}
        employees.post(employee_put_args, True, args)
        db.Librarians.insert_one(new_args)
        del new_args['_id']

        return new_args, 201