from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.content import Content, ContentCreate, ContentUpdate
from typing import List, Dict, Any, Optional
from datetime import datetime
from bson import ObjectId

router = APIRouter()

# --- Section Configuration ---
# In a real app, this might be in DB, but for now we define the structure here.
PAGES_CONFIG = {
    "home": [
        {"name": "hero", "type": "hero", "label": "Main Hero Section"},
        {"name": "features", "type": "cards", "label": "Core Features"},
    ],
    "about": [
        {"name": "hero", "type": "hero", "label": "About Hero"},
        {"name": "team", "type": "cards", "label": "Management Team"},
        {"name": "mission_vision", "type": "text", "label": "Mission & Vision"},
    ],
    "services": [
        {"name": "hero", "type": "hero", "label": "Services Hero"},
        {"name": "service_list", "type": "cards", "label": "Service Cards"},
    ],
    "news": [
        {"name": "hero", "type": "hero", "label": "News Hero"},
        {"name": "latest_news", "type": "cards", "label": "Latest News"},
    ],
    "blog": [
        {"name": "hero", "type": "hero", "label": "Blog Hero"},
        {"name": "posts", "type": "cards", "label": "Blog Posts"},
    ]
}

# backend/app/api/cms.py

@router.get("/sections") # This will be /api/admin/cms/sections
async def get_sections(page: str = "home"): # Add a default value
    # Normalize the page name to lowercase
    page_key = page.lower()
    if page_key not in PAGES_CONFIG:
        # If the page isn't found, return an empty list instead of 404 
        # to prevent the frontend from crashing.
        return [] 
    return PAGES_CONFIG[page_key]


@router.get("/content", response_model=Optional[Content])
async def get_content(page: str, section: str, db = Depends(get_database)):
    doc = await db["content"].find_one({"page": page, "section": section})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

@router.put("/content", response_model=Content)
async def upsert_content(item: ContentCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    
    # Check if exists
    existing = await db["content"].find_one({"page": item.page, "section": item.section})
    
    if existing:
        await db["content"].update_one(
            {"_id": existing["_id"]},
            {"$set": update_data}
        )
        update_data["_id"] = str(existing["_id"])
    else:
        update_data["created_at"] = datetime.utcnow()
        result = await db["content"].insert_one(update_data)
        update_data["_id"] = str(result.inserted_id)
    
    return update_data

@router.put("/content/{id}/publish")
async def publish_content(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["content"].update_one(
        {"_id": ObjectId(id)},
        {"$set": {"status": "published", "updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    
    updated = await db["content"].find_one({"_id": ObjectId(id)})
    updated["_id"] = str(updated["_id"])
    return updated

@router.get("/activity")
async def get_activity(db = Depends(get_database), admin: str = Depends(get_current_admin)):
    activity = []
    async for doc in db["content"].find().sort("updated_at", -1).limit(5):
        activity.append({
            "id": str(doc["_id"]),
            "page": doc["page"],
            "section": doc["section"],
            "status": doc["status"],
            "updated_at": doc.get("updated_at", doc.get("created_at"))
        })
    return activity

