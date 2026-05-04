from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class BlogBase(BaseModel):
    title: str = Field(..., max_length=200)
    slug: str = Field(..., max_length=200)
    content: str = Field(...)
    author: Optional[str] = "Admin"
    thumbnail_url: Optional[str] = None

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    content: Optional[str] = None

class Blog(BlogBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: Optional[datetime] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
