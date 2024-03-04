from typing import List
from pydantic import BaseModel


class FilterParams(BaseModel):
    tags: List[str]


# Temporarily unused (need to add infra to mongodb)
# class Image(BaseModel):
#     filename: str
#     path: str


class Lookbook(BaseModel):
    # id: str = Field(alias="_id", default=None) # Needs extra config to convert objectID to pydantic supported type
    lookbook_name: str
    tags: List[str]
    # images: List[Image]
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
