import re
import pymongo
client = pymongo.MongoClient(host = 'localhost',port = 27017)
db = client.test
collection = db.test1
dict1 = {'aa':1, 'bb':2, 'cc':3}
collection.insert(dict1)
