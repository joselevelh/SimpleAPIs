from fastapi import FastAPI
from models import FilterParams, Image, Lookbook
import crud

app = FastAPI(title="Unofficial Drakes Lookbook API",
              summary="An API to browse Drakes lookbooks", )


@app.get("/lookbooks/{title}")
async def get_lookbook(title: str):
    print(f"Searching for {title} in lookbooks db...")
    return crud.retrieve_lookbook_by_name(name=title)


@app.get("/lookbooks/id/{id}")
async def get_lookbook(object_id: str):
    print(f"Searching for {object_id} in lookbooks db...")
    return crud.retrieve_lookbook_by_object_id(object_id=object_id)


@app.get("/lookbooks/all")
async def get_or_filtered_lookbooks(filter_params: FilterParams):
    """Returns lookbooks that match ALL the tags given"""
    # Use 'filter_params.tags' to filter lookbooks
    # ...
    return None


@app.get("/lookbooks/any")
async def get_and_filtered_lookbooks(filter_params: FilterParams):
    """Returns lookbooks that math ANY of the tags given"""
    # Use 'filter_params.tags' to filter lookbooks
    # ...
    return None

