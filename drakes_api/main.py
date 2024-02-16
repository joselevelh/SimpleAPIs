from fastapi import FastAPI
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
