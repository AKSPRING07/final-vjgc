from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated, Dict, Any, List
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ContentBase(BaseModel):
    page: str # home, about, services
    subpage: Optional[str] = None # about-group, leadership, etc.
    section: str # hero, cards, features
    type: str # hero, cards, text
    content: Optional[Any] = None # Dynamic JSON content (Dict or List)
    status: str = "draft" # draft, published
    versions: Optional[List[Dict[str, Any]]] = None # List of previous contents
    
    # Optional fields for granular card actions
    action: Optional[str] = None # create_card, update_card, delete_card
    card_id: Optional[str] = None # ID of the card being updated or deleted
    data: Optional[Dict[str, Any]] = None # Data for the specific card operation

class ContentCreate(ContentBase):
    pass

class ContentUpdate(BaseModel):
    content: Optional[Any] = None
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

class BusinessCardCreate(BaseModel):
    mainPage: str
    subSection: str
    category: str
    title: str
    description: str
    image: str
