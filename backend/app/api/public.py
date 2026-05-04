from fastapi import APIRouter, Depends
from app.db.mongodb import get_database
from app.schemas.achievement import Achievement
from typing import List

router = APIRouter()

@router.get("/achievements", response_model=List[Achievement])
async def list_achievements(db = Depends(get_database)):
    """Public API to fetch achievements."""
    achievements = []
    cursor = db["achievements"].find().limit(100)
    async for document in cursor:
        if "_id" in document:
            document["_id"] = str(document["_id"])
        achievements.append(document)
    return achievements
