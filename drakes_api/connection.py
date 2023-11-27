from pymongo import MongoClient

MONGO_URI = "mongodb+srv://joselevel:ItOnuTIkP7rDsO5Z@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)