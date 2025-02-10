from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
import time

# Connect to your Atlas deployment
client = MongoClient('localhost:27017',
                     username='root',
                     password='password',
                     authSource='admin',
                     authMechanism='SCRAM-SHA-256')

database = client["testingdb"]
collection = database["testingcollection"]

collection.insert_one({"f":"g"})

results = collection.find()
for record in results:
    print(record)
