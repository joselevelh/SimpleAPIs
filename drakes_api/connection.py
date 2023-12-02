from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"

new_lookbook = [
    {
        "lookbook_name": "spring-summer-2017-lookbook",
        "tags": ["spring-summer", "2017", "casual", "menswear"],
        "images": [
            "/images/spring-summer-2017-lookbook/image_22.jpg",
            "/images/spring-summer-2017-lookbook/image_21.jpg",
            "/images/spring-summer-2017-lookbook/image_20.jpg",
            "/images/spring-summer-2017-lookbook/image_19.jpg",
            "/images/spring-summer-2017-lookbook/image_18.jpg",
            "/images/spring-summer-2017-lookbook/image_17.jpg",
            "/images/spring-summer-2017-lookbook/image_11.jpg",
            "/images/spring-summer-2017-lookbook/image_10.jpg",
            "/images/spring-summer-2017-lookbook/image_9.jpg",
            "/images/spring-summer-2017-lookbook/image_8.jpg",
            "/images/spring-summer-2017-lookbook/image_7.jpg",
            "/images/spring-summer-2017-lookbook/image_3.jpg",
            "/images/spring-summer-2017-lookbook/image_1.jpg"
        ]
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
    db = client.drakes_lookbooks
    lookbooks_collection = db.lookbooks
    result = lookbooks_collection.insert_many(new_lookbook)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    client.close()


except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
