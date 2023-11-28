from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)
    # Check the connection by listing database names
    print(f"Client: {client}")
    database_names = client.list_databases()
    print("Connected to MongoDB. Database names:")
    for db_name in database_names:
        print(db_name)


except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
