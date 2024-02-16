from pymongo import MongoClient
from bson.objectid import ObjectId
from models import Lookbook
import pydantic

# MongoDB Setup
MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.drakes_lookbooks
lookbooks_collection = db.lookbooks


def check_db_connection():
    check = 0
    if client:
        print(f"Connection to MongoDB client: {client}")
        check += 1
    if db is not None:
        print(f"Lookbook DB: {db}")
        check += 1
    if db.lookbooks is not None:
        print(f"Lookbook collection: {db.lookbooks}")
        check += 1
    return check == 3


def retrieve_lookbook_by_name(name: str) -> Lookbook:
    search_ex = {"lookbook_name": name}
    print(f"Search expression: {search_ex}")
    result = lookbooks_collection.find_one(search_ex)
    print(f"Lookbook: {result}")
    return result
