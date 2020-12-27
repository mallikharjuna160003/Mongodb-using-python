import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
#print(myclient.list_database_names())

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("Database not exist.")

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
else:
  print("The collection does not exists.")
