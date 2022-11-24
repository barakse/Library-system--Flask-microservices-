import sys
#sys.path.insert(0,'..')
#sys.path.append('../')
#sys.path.append('../Services')
from importlib import import_module
from os import abort
from flask import Flask	
from flask_restful import Api

from Services.BookService import books, book


app = Flask(__name__)
api = Api(app)

api.add_resource(book, "/books/<int:book_id>")
api.add_resource(books, "/books")
api.add_resource(books, "/books/add", methods=['POST'], endpoint = 'add')
api.add_resource(book, "/books/update/<int:book_id>",  methods=['PUT'], endpoint = 'update')

def main():
    app.run( port=8000, debug=True)

if __name__ == "__main__":
	main()