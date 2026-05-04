from pydantic import BaseModel
from typing import Optional

class AboutBase(BaseModel):
    title: str
    description: str
    mission: Optional[str] = None
    vision: Optional[str] = None
    image_url: Optional[str] = None

class AboutCreate(AboutBase):
    pass

class AboutUpdate(AboutBase):
    title: Optional[str] = None
    description: Optional[str] = None

class About(AboutBase):
    id: int

    class Config:
        from_attributes = True
