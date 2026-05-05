from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ServiceBase(BaseModel):
    title: str = Field(..., max_length=100)
    icon: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = "Published"
    is_active: bool = True

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    name: Optional[str] = None
    summary: Optional[str] = None

class Service(ServiceBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
