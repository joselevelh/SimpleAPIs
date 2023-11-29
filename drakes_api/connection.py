from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

try:
    client = MongoClient(MONGO_URI)
    # Check the connection by listing database names
    print(f"Client: {client}")
    database_names = client.list_databases()
    print("Connected to MongoDB. Database names:")
    for db_name in database_names:
        print(db_name)
    db = client.bank
    accounts_collection = db.accounts
    result = accounts_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    client.close()


except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
