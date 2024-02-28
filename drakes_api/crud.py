from pymongo import MongoClient
from models import Lookbook

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




def retrieve_lookbook_by_tag(tags: list[str]) -> list[Lookbook]:
    query = {"tags": {"$in": tags}}  # $in does partial matching in mongo array
    matching_lookbooks = lookbooks_collection.find(query)
    return matching_lookbooks


def retrieve_lookbook_by_name(name: str) -> list[Lookbook]:
    query = {"$text": {"$search": name}, "$limit": 10}
    print(f"{query= }")
    result: list[Lookbook] = lookbooks_collection.find(query)
    for lookbook in result:
        print(f"{lookbook= }")
    return result
