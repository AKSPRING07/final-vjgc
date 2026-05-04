from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime
from pydantic.functional_validators import BeforeValidator

# Helper to handle MongoDB ObjectId as string
PyObjectId = Annotated[str, BeforeValidator(str)]

class AchievementBase(BaseModel):
    title: str = Field(..., example="Winner of Tech Excellence 2024")
    description: Optional[str] = Field(None, example="Awarded for outstanding innovation in AI.")
    date: Optional[str] = Field(None, example="2024-05-01")
    image_url: Optional[str] = None

class AchievementCreate(AchievementBase):
    pass

class AchievementUpdate(AchievementBase):
    title: Optional[str] = None

class Achievement(AchievementBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: Optional[datetime] = None # Make it optional so old records don't crash

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True
    )
