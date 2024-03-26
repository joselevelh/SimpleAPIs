import os

from app.crud import client

import typer


app = typer.Typer()
google_storage_bucket_base = "https://storage.googleapis.com/drakes_lookbooks_bucket/drakes_images/"


def iterate_subdirectories(directory_path: str):
    """
    Iterate through subdirectories within the specified directory path.
    """
    # Check if the path exists
    if not os.path.exists(directory_path):
        typer.echo("The specified path does not exist.")
        raise typer.Exit()

    # Check if the path is a directory
    if not os.path.isdir(directory_path):
        typer.echo("The specified path is not a directory.")
        raise typer.Exit()

    # Iterate through directories and subdirectories
    for root, directories, _ in os.walk(directory_path):
        for lookbook in directories:
            lookbook_path = os.path.join(root, lookbook)
            for _, _, files in os.walk(lookbook_path):
                image_paths = [google_storage_bucket_base + lookbook + "/" + image_name for image_name in files]
                new_lookbook = create_lookbook_dict(lookbook_name=lookbook, lookbook_tags=[], image_paths=image_paths)
                upload_lookbook(new_lookbook)


def create_lookbook_dict(lookbook_name: str, lookbook_tags: list, image_paths: list[str]) -> list[dict]:
    new_lookbook = [
        {
            "lookbook_name": lookbook_name,
            "tags": lookbook_tags,
            "images": image_paths
        },
    ]
    typer.echo(f"{new_lookbook= }")
    return new_lookbook


def upload_lookbook(lookbooks_to_upload: list[dict]):
    """Uploads given lookbook to Google Cloud"""

    try:

        # Check the connection by listing database names
        print(f"Client: {client}")
        database_names = client.list_databases()
        print("Connected to MongoDB. Database names:")
        for db_name in database_names:
            print(db_name)
        db = client.drakes_lookbooks
        lookbooks_collection = db.lookbooks
        result = lookbooks_collection.insert_many(lookbooks_to_upload)

        document_ids = result.inserted_ids
        print("# of documents inserted: " + str(len(document_ids)))
        print(f"_ids of inserted documents: {document_ids}")

        client.close()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


@app.command()
def main(directory_path: str):
    """
    Iterate through subdirectories within the specified directory path.
    """
    iterate_subdirectories(directory_path)


if __name__ == "__main__":
    app()
