import pymongo


dbName = "yourDBName"
json_data = []
###########python -m pip install pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
myDb = client["scarbfun"]
myCollection = myDb[dbName]
res = myCollection.insert_one(json_data)