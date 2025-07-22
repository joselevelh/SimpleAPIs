from bson import ObjectId
from pymongo import MongoClient
from app.models import Lookbook
import os

# MongoDB Setup
MONGO_URI = os.getenv("MONGO_URI")
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
    if db.lookbooks.find_one({"lookbook_name": "spring-summer-2017-lookbook"}) is not None:
        print(f'Lookbook = {db.lookbooks.find_one({"lookbook_name": "spring-summer-2017-lookbook"})}')
        check += 1
    return check == 4


def retrieve_lookbook_by_tag(tags: list[str], cursor=None, limit: int = 5) -> list[Lookbook]:
    query = {"tags": {"$in": tags}}  # $in does partial matching in mongo array
    if cursor:
        query["_id"] = {"$lt": ObjectId(cursor)}
    matching_lookbooks = lookbooks_collection.find(query).sort("_id", -1).limit(limit)
    lookbook_list = []
    for doc in matching_lookbooks:
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        lookbook_list.append(Lookbook(**doc))
    return lookbook_list


def retrieve_lookbook_by_name(name: str, cursor=None, limit: int = 5) -> list[Lookbook]:
    query = {"$text": {"$search": name}}
    if cursor:
        query["_id"] = {"$lt": ObjectId(cursor)}
    matching_lookbooks = lookbooks_collection.find(query).sort("_id", -1).limit(limit)
    lookbook_list = []
    for doc in matching_lookbooks:
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        lookbook_list.append(Lookbook(**doc))
    return lookbook_list
