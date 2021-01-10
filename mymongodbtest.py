from pymongo import MongoClient
con = MongoClient(host="127.0.0.1",port=27017,username="admin",password="admin")
db = con["mytestdb"]
mycol = db["mydata"]
mycol.insert_one({"A":10})
db_result = mycol.find()
for i in db_result:
   print(i["A"])
