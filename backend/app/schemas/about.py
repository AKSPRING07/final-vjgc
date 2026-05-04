from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class AboutBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(...)
    mission: Optional[str] = None
    vision: Optional[str] = None
    image_url: Optional[str] = None

class AboutCreate(AboutBase):
    pass

class AboutUpdate(AboutBase):
    title: Optional[str] = None
    description: Optional[str] = None

class About(AboutBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
