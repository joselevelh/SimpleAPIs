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
        "https://yourdomain.com",  # Todo: Change this to my front-end domain
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
def get_lookbook(title: str) -> list[Lookbook]:
    print(f"Searching for {title} in lookbooks db...")
    lookbooks = crud.retrieve_lookbook_by_name(name=title)
    print(f"{lookbooks=}")
    return lookbooks


@app.get("/lookbooks/any/")
def get_lookbooks_any(tags: list[str] = Query(default=None),
                      limit: int = 5,
                      cursor=None) -> LookbookResponse:
    """Returns all lookbooks that have the given tag(s)"""
    print(f"Searching for {tags} in lookbooks db...")
    lookbooks = list(crud.retrieve_lookbook_by_tag(tags=tags, cursor=cursor, limit=limit))
    print(f"{lookbooks=}")
    lb_response = LookbookResponse(
        lookbooks_list=lookbooks,
        next_cursor=lookbooks[-1].id,  # The id of the last lb we got
        has_more=len(lookbooks) == limit  # If we reached limit there might be more
    )
    return lb_response
