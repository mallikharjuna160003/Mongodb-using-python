import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#ascending order sorting
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x) 

#descending order sorting

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x) 
