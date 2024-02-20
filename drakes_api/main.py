from typing import List

from fastapi import FastAPI, Query
# from models import FilterParams, Image, Lookbook
from models import FilterParams, Lookbook
import crud


app = FastAPI(title="Unofficial Drakes Lookbook API",
              summary="An API to browse Drakes lookbooks", )


@app.get("/syscheck")
async def system_check():
    print(f"Starting system check for API and DB connection")
    return crud.check_db_connection()


@app.get("/lookbooks/{title}")
async def get_lookbook(title: str) -> Lookbook:
    print(f"Searching for {title} in lookbooks db...")
    lookbook = crud.retrieve_lookbook_by_name(name=title)
    print(f"{lookbook =}")
    return lookbook


@app.get("/lookbooks/any/")
async def get_lookbooks_any(tags: list[str] = Query(default=None)) -> list[Lookbook]:
    """Returns all lookbooks that have the given tag(s)"""
    print(f"Searching for {tags} in lookbooks db...")
    lookbooks = crud.retrieve_lookbook_by_tag(tags=tags)
    print(f"{lookbooks =}")
    return lookbooks


@app.get("/lookbooks/all")
async def get_lookbooks_all(filter_params: FilterParams):
    """Returns lookbooks that match ALL the tags given"""
    # Use 'filter_params.tags' to filter lookbooks
    # ...
    return None
