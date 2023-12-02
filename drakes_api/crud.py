from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB Setup
MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.drakes_lookbooks
lookbooks_collection = db.lookbooks


def retrieve_lookbook_by_name(name: str):
    search_ex = {"lookbook name": name}
    print(f"Search expression: {search_ex}")
    result = lookbooks_collection.find_one(search_ex)
    return result


def retrieve_lookbook_by_object_id(object_id: str):
    search_ex = {"_id": ObjectId(object_id)}
    print(f"Search expression: {search_ex}")
    result = lookbooks_collection.find_one(search_ex)
    return result
