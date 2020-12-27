import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#x = mycol.find_one()
#print(x) 

for x in mycol.find():  # it is just like select * 
    print(x)


for x in mycol.find({},{"_id":0,"name":1,"address":1}):  # it is just like select * 
    print(x)



for x in mycol.find({},{"address":0}):  # it is just like select * 
    print(x)

#the following give error 
#for x in mycol.find({},{"name":1,"address":0}):  # it is just like select * 
 #   print(x)
