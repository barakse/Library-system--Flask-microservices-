from pymongo import MongoClient

cluster = "mongodb+srv://barakse222:123MongoDB@library-flask.censagw.mongodb.net/Library-Flask?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(cluster)

print(client.list_database_names())

db = client["Library-Flask"]
print(db.list_collection_names())
my_collection = db["Employees"]

#==================FROM DATA2====================
#db.runCommand( { collMod: "Employees",validator={
 #   validator})
 
def buildCollection(name):
    if name not in db.list_collection_names():
        db.create_collection(name)
    
    #db.command("collMod", name, validator=validatork)
try:
    buildCollection("Employees")
    print(db.list_collection_names())
except:
    print("FAILED")
#buildCollection("Librarians", librarian_validator)
#buildCollection("Books", book_validator)