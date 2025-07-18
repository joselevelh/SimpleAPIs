from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    tags: List[str]


class Lookbook(BaseModel):
    id: str = Field(alias="_id")  # Maps MongoDB's _id to id
    lookbook_name: str
    tags: List[str]
    images: List[str]

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "lookbook_name": "spring-summer-2017-lookbook",
                "tags": ["spring-summer", "2017", "casual", "menswear"],
                "images": ["/images/spring-summer-2017-lookbook/image_3.jpg",
                           "/images/spring-summer-2017-lookbook/image_1.jpg"]}
        }


class LookbookResponse(BaseModel):
    lookbooks_list: list[Lookbook]
    has_more: bool
    next_cursor: str | None
