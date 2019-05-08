import sys
from pymongo import MongoClient, ReturnDocument

if len(sys.argv) != 2:
    exit("Usage: {} name".format(sys.argv[0]))

name = sys.argv[1]

connector = "mongodb://localhost"
client = MongoClient(connector)
db = client.mydb


res = db.counter.find_one_and_update( { '_id': name }, { '$inc' : {'value' : 1 } }, upsert = True, return_document=ReturnDocument.AFTER)

print(res)


