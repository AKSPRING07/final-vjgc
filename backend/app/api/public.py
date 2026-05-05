from fastapi import APIRouter, Depends
from app.db.mongodb import get_database
from app.schemas.achievement import Achievement
from app.schemas.about import About
from app.schemas.service import Service
from app.schemas.blog import Blog
from typing import List, Optional

router = APIRouter()

@router.get("/about", response_model=About)
async def get_about(db = Depends(get_database)):
    """Fetch About Us content."""
    about = await db["about"].find_one()
    if about:
        about["_id"] = str(about["_id"])
    return about

@router.get("/achievements", response_model=List[Achievement])
async def list_achievements(db = Depends(get_database)):
    """List all achievements."""
    achievements = []
    cursor = db["achievements"].find().limit(100)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        achievements.append(doc)
    return achievements

@router.get("/services", response_model=List[Service])
async def list_services(db = Depends(get_database)):
    """List all services."""
    services = []
    cursor = db["services"].find().limit(100)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        services.append(doc)
    return services

@router.get("/news", response_model=List[Blog])
async def list_news(db = Depends(get_database)):
    """List all news/blog posts."""
    blogs = []
    cursor = db["news"].find().limit(100)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        blogs.append(doc)
    return blogs

@router.get("/cms/content", response_model=Optional[dict])
async def get_published_content(page: str, section: str, db = Depends(get_database)):
    """Fetch published CMS content for a specific page and section."""
    doc = await db["content"].find_one({"page": page, "section": section, "status": "published"})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc
