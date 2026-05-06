from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated, Dict, Any, List
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class UniversalContentBase(BaseModel):
    mainPage: str
    subSection: str
    category: str
    title: str
    description: str
    image: str
    order: Optional[int] = 0
    isActive: bool = True

class UniversalContentCreate(UniversalContentBase):
    pass

class UniversalContentUpdate(BaseModel):
    mainPage: Optional[str] = None
    subSection: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    order: Optional[int] = None
    isActive: Optional[bool] = None

class UniversalContent(UniversalContentBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
