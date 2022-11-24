#from ..Controllers import EmployeeController
from flask_restful import Api, Resource, reqparse, abort
from Data import employee_put_args
import json
import sys
sys.path.append('../')
#from Models import Employee, Librarian
from Models.Employee import Employee
#from Models.Librarian import Librarian
import string

def check_if_key_in_JSON_file_dict(id,path):

    with open(path) as openJson:
        dict = json.load(openJson)
    return str(id) in dict

def abort_if_employee_id_dosent_exist(employee_id):
    with open('./DB/employees_dict.json', 'r') as openfile:
        empolyees_dict = json.load(openfile)
    s = str(employee_id)
    if s not in empolyees_dict:
        abort(404, message="couldnt find, isnt VALID...")

def abort_if_empolyee_exists(employee_id):
    with open('./DB/employees_dict.json', 'r') as openfile:
        empolyees_dict = json.load(openfile)
    print(empolyees_dict)
    if employee_id in empolyees_dict:
        abort(409, message="empolyee already exists with that ID...")

'''def put(self,video_id):

		#abort_if_video_exists(video_id)

		args = video_put_args.parse_args()
		videos[video_id] = args
		return videos[video_id], 201 
		
	def delete(self, video_id):
		#abort_if_video_id_dosent_exist(video_id)

		del videos[video_id]
		return '', 204
    def insider get
   
'''
class employee(Resource):
    def get(self, employee_id):
        print("Spec get")

        abort_if_employee_id_dosent_exist(employee_id)
        with open('./DB/employees_dict.json', 'r') as openfile:
            empolyees_dict = json.load(openfile)
           
        return empolyees_dict[str(employee_id)]
    
    def delete(self, employee_id):
        abort_if_employee_id_dosent_exist(employee_id)
        with open('./DB/employees_dict.json','r') as f:
            employees_dict = json.load(f)
        
        item_removed = employees_dict[str(employee_id)]
        employees_dict[str(employee_id)]['isFired'] = True

        with open('./DB/employees_dict.json','w') as f:
            json.dump(employees_dict,f)

        if check_if_key_in_JSON_file_dict(employee_id,'./DB/librarian_dict.json'):
            with open('./DB/librarian_dict.json','r') as f:
                librarian_dict = json.load(f)
        
            item_removed = librarian_dict[str(employee_id)]
            librarian_dict[str(employee_id)]['isFired'] = True

            with open('./DB/librarian_dict.json','w') as f:
                json.dump(librarian_dict,f)
    
        return item_removed,202

class employees(Resource):

    def get(self):
        print("Reg get")
        with open('./DB/employees_dict.json', 'r') as openfile:
            empolyees_dict = json.load(openfile)
        return empolyees_dict
    '''def post_employee(self, data):
        args = employee_put_args.parse_args()
        empolyees_dict[args.id] = args

        #empolyees_dict.update({args.id: args})
        return empolyees_dict[args.id], 201
    '''
    def post(self):
            args = employee_put_args.parse_args()
            abort_if_empolyee_exists(args.id)
            print("Continue posting")
            '''
            with open("./DB/employees_dict.json", "r+") as outfile:
                data = json.load(outfile)
                print(data)
                data.update({args.id:args})
                json.dump(data, outfile)
                #json.dump({args.id:args}, outfile)
            '''
            with open('./DB/employees_dict.json','r') as f:
                dict = json.load(f)

            #new_Employee = Employee(args.id, args.name, args.age)
            #print(new_Employee.__dict__)
            args.isFired = False
            dict.update({args.id:args})

            with open('./DB/employees_dict.json','w') as f:
                json.dump(dict,f)
             
                
            print("Hey sugar")
            return args, 201

class librarians(Resource):
    def post(self):
        print("Librar until i die")

        args = employee_put_args.parse_args()
        abort_if_empolyee_exists(args.id)
        
        with open('./DB/librarian_dict.json','r') as f:
            dict = json.load(f)

        args.isFired = False
        dict.update({args.id:args})

        with open('./DB/librarian_dict.json','w') as f:
            json.dump(dict,f)
        
        print(args)

        args2 = args.copy()
        del args2['yearsOfExperience']
        #with open("./DB/employees_dict.json", "w") as outfile:
         #   json.dump({args.id:args}, outfile)
        with open('./DB/employees_dict.json','r') as f:
            dict = json.load(f)

        dict.update({args.id:args2})

        with open('./DB/employees_dict.json','w') as f:
            json.dump(dict,f)

        return args, 201