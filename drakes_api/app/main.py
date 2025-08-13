from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware

from app.models import Lookbook, LookbookResponse
from app import crud

app = FastAPI(title="Unofficial Drakes Lookbook API",
              summary="An API to browse Drakes lookbooks", )

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5173/",
        "https://bionic-freehold-415417.web.app",
        "https://the-lilas.com/",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/syscheck")
def system_check():
    print(f"Starting system check for API and DB connection")
    return crud.check_db_connection()


@app.get("/lookbooks/{title}")
def get_lookbook(title: str,
                 limit: int = 2,
                 cursor=None) -> LookbookResponse:
    print(f"Searching for {title} in lookbooks db...")
    lookbooks = crud.retrieve_lookbook_by_name(name=title, cursor=cursor, limit=limit)
    print(f"{lookbooks=}")
    # Handle empty results
    next_cursor = ""
    if lookbooks:  # Only set cursor if we have results
        next_cursor = lookbooks[-1].id  # The id of the last lb we got
    lb_response = LookbookResponse(
        lookbooks_list=lookbooks,
        next_cursor=next_cursor,
        has_more=len(lookbooks) == limit  # If we reached limit there might be more
    )
    return lb_response


@app.get("/lookbooks/any/")
def get_lookbooks_any(tags: list[str] = Query(default=None),
                      limit: int = 2,
                      cursor=None) -> LookbookResponse:
    """Returns all lookbooks that have the given tag(s)"""
    print(f"Searching for {tags} in lookbooks db...")
    lookbooks = crud.retrieve_lookbook_by_tag(tags=tags, cursor=cursor, limit=limit)
    print(f"{lookbooks=}")
    # Handle empty results
    next_cursor = ""
    if lookbooks:  # Only set cursor if we have results
        next_cursor = lookbooks[-1].id  # The id of the last lb we got
    lb_response = LookbookResponse(
        lookbooks_list=lookbooks,
        next_cursor=next_cursor,
        has_more=len(lookbooks) == limit  # If we reached limit there might be more
    )
    return lb_response


@app.get("/lookbooks/untagged/")
def get_untagged_lookbooks(limit: int = 2,
                           cursor=None) -> LookbookResponse:
    """Returns all untagged lookbooks"""
    print(f"Searching for untagged lookbooks db...")
    lookbooks = crud.retrieve_untagged_lookbooks(cursor=cursor, limit=limit)
    print(f"{lookbooks=}")
    # Handle empty results
    next_cursor = ""
    if lookbooks:  # Only set cursor if we have results
        next_cursor = lookbooks[-1].id  # The id of the last lb we got
    lb_response = LookbookResponse(
        lookbooks_list=lookbooks,
        next_cursor=next_cursor,
        has_more=len(lookbooks) == limit  # If we reached limit there might be more
    )
    return lb_response
