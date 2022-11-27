from os import abort
from flask import Flask, request	
from flask_restful import Api, abort
import requests

EMPLOYEEBASE = "http://127.0.0.1:5000/"
BOOKBASE= "http://127.0.0.1:8000/"

app = Flask(__name__)
api = Api(app)

async def get(path):
    return requests.get(path)
async def post(path, data):
    return requests.post(path, data)
async def delete(path):
    return requests.delete(path)
async def put(path, data):
    return requests.put(path,data)

async def directToService(request, basic_path):
    response = None
    req_str = request.base_url
    new_url = basic_path +  req_str[len(basic_path):] 
    args = dict(request.form)

    if request.method == 'GET':
        response = await get(new_url)
    elif request.method == 'DELETE':
        response = await delete(new_url)  
    elif request.method == 'POST':
        response = await post(new_url,args) 
    elif request.method == 'PUT':
        response = await put(new_url, args)  

    return response

@app.route('/')
@app.route('/<string:service>', methods = ['GET','POST'])
@app.route('/<string:service>/<int:id>', methods = ['DELETE','GET'])
@app.route('/<string:service>/<string:domain1>', methods = ['GET','POST', 'PUT'])
@app.route('/<string:service>/<string:domain1>/<string:domain2>',  methods = ['POST','PUT'])
async def index(service = "Bye", id = None, domain1 = None, domain2 = None):
    response = None
    if service == 'employees':
        response = await directToService(request, EMPLOYEEBASE)

    elif service == 'books':
        response = await directToService(request, BOOKBASE)

    if response is None:
        abort(404)

    return response.json()

def main():
    app.run(port=9000, debug=True)

if __name__ == "__main__":
	main()
