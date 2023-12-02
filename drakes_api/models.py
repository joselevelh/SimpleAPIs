from typing import List
from pydantic import BaseModel


class FilterParams(BaseModel):
    tags: List[str]


class Image(BaseModel):
    filename: str
    path: str


class Lookbook(BaseModel):
    lookbook_name: str
    tags: List[str]
    images: List[Image]
