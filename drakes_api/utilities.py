from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user2:x7s1uNrJePt7ZvCq@cluster1.rdtlrgq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.drakes_lookbooks


def renew_index():
    try:
        lookbooks_collection = db.lookbooks
        lookbooks_collection.create_index([('lookbook_name', 'text')])
        print(lookbooks_collection.index_information())
        client.close()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


def update_lookbook_tags(lookbook_name: str, tags_to_add: list[str], replace: bool = False):
    """Updates tag of document, returns True if there is any change in the tag field after operation"""
    if replace:
        existing_tags = db.lookbooks.find_one({"lookbook_name": lookbook_name}).get('tags')
        db.lookbooks.update_one(
            {"lookbook_name": lookbook_name},
            {"$set": {"tags": tags_to_add}},
        )
        new_tags = db.lookbooks.find_one({"lookbook_name": lookbook_name}).get('tags')
        print(f"Updated tags for {lookbook_name}:"
              f"\t old tags: {existing_tags}"
              f"\t new tags: {new_tags}")
        return new_tags == tags_to_add
    else:
        print(f"Updated tags for {lookbook_name}:")
        existing_tags: list[str] = db.lookbooks.find_one({"lookbook_name": lookbook_name}).get('tags')
        print(f"\t old tags: {existing_tags}")
        updated_tags = existing_tags
        for tag in tags_to_add:
            updated_tags.append(tag)
        db.lookbooks.update_one(
            {"lookbook_name": lookbook_name},
            {"$set": {"tags": updated_tags}},
        )
        new_tags: list[str] = db.lookbooks.find_one({"lookbook_name": lookbook_name}).get('tags')
        print(f"\t new tags: {new_tags}")
        return new_tags != existing_tags


if __name__ == "__main__":
    # update_lookbook_tags(lookbook_name="autumn-in-paris-lookbook",
    #                      tags_to_add=["autumn", "fall", "city", "paris", "hat", "cap", "sweater", "jeans"],
    #                      replace=True)
    pass
