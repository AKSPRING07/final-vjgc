from pydantic import BaseModel
from typing import Optional

class ServiceBase(BaseModel):
    name: str
    icon: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    is_active: Optional[bool] = True

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    name: Optional[str] = None

class Service(ServiceBase):
    id: int

    class Config:
        from_attributes = True
