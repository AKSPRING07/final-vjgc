from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated, Dict, Any
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ContentBase(BaseModel):
    page: str # home, about, services
    section: str # hero, cards, features
    type: str # hero, cards, text
    content: Dict[str, Any] # Dynamic JSON content
    status: str = "draft" # draft, published

class ContentCreate(ContentBase):
    pass

class ContentUpdate(BaseModel):
    content: Optional[Dict[str, Any]] = None
    status: Optional[str] = None

class Content(ContentBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
