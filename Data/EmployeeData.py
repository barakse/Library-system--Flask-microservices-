from dbConnection import db
from flask_restful import abort

db_Employees = db.get_collection("Employees")
db_Librarians = db.get_collection("Librarians")

class EmployeeData:
    def abort_if_id_isnt_valid(self,id, db_collection, is_exist):
        if ((db[db_collection].find_one({"id": id}) is None) == is_exist):
            if(is_exist):
                abort(404, message="This ID dosent exist in " + db_collection)
                
            else:
                abort(409, message="This ID already exist in " + db_collection) 
            
    def get_employee(self, id):
        return db_Employees.find_one({'id': id}, {'_id':0})

    def delete_employee(self, id):
        return db_Employees.find_one_and_update({'id':id},{"$set":{'isFired':True}},{'_id':0})

    def get_employees(self):
        empolyees_dict = list(db_Employees.find({}, {'_id': False}))
        print(empolyees_dict[0] if len(empolyees_dict) == 1 else empolyees_dict)
        return empolyees_dict[0] if len(empolyees_dict) == 1 else empolyees_dict
        
    def post_employees(self, args):
            db_Employees.insert_one(args)
            
    def post_librarian(self, args):
        db_Librarians.insert_one(args) #data

    