from pymongo import MongoClient

cluster = "mongodb+srv://barakse222:123MongoDB@library-flask.censagw.mongodb.net/Library-Flask?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(cluster)

print(client.list_database_names())

db = client["Library-Flask"]
print(db.list_collection_names())
my_collection = db["Employees"]
