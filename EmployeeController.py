import sys
#sys.path.insert(0,'..')
#sys.path.append('../')
from importlib import import_module
from os import abort
from flask import Flask	
from flask_restful import Api, Resource, reqparse, abort

from Services.service import employees, librarians, employee



""""
names = {"tim":{"age":19,"gender": "male"},
	 	"bill":{"age":70,"gender": "male"}}
class HelloWorld(Resource): #inheirt from resource -> handle get/put/delete
	def get(self,name):
		return names[name]
	def post(self):
		return {"data": "Posted"}
api.add_resource(HelloWorld,"/helloworld/<string:name>")
"""
app = Flask(__name__)
api = Api(app)

api.add_resource(employee, "/employees/<int:employee_id>")
api.add_resource(employees, "/employees", endpoint = 'get')
api.add_resource(employees, "/employees/add", methods=['POST'], endpoint = 'STAM')
api.add_resource(librarians, "/employees/librarian/add",  methods=['POST'])

#/<int:test>
def main():
	app.run(debug=True)

if __name__ == "__main__":
	main()