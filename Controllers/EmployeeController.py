from flask import Flask	
from flask_restful import Api
import sys
sys.path.append('../')
from Services.service import employees, librarians, employee

app = Flask("Employee-Librarian")
api = Api(app)

api.add_resource(employee, "/employees/<int:employee_id>")
api.add_resource(employees, "/employees", endpoint = 'get')
api.add_resource(employees, "/employees/add", methods=['POST'], endpoint = 'STAM')
api.add_resource(librarians, "/employees/librarian/add",  methods=['POST'])

def main():
	app.run(debug=True)

if __name__ == "__main__":
	main()