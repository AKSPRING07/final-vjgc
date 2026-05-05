from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.achievement import Achievement, AchievementCreate
from app.schemas.about import About, AboutUpdate
from app.schemas.service import Service, ServiceCreate
from app.schemas.blog import Blog, BlogCreate
from typing import List
from datetime import datetime
import uuid
import shutil
import os

router = APIRouter()

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "gif"}

# --- Media Management ---
@router.post("/media/upload")
async def upload_image(file: UploadFile = File(...), admin: str = Depends(get_current_admin)):
    try:
        file_ext = file.filename.split(".")[-1].lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail=f"Invalid file type: {file_ext}")
        
        unique_filename = f"{uuid.uuid4()}.{file_ext}"
        # Ensure directory exists
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
            
        file_path = os.path.join(UPLOAD_DIR, unique_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        return {"url": f"/uploads/{unique_filename}", "filename": unique_filename}
    except Exception as e:
        print(f"Upload Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# --- About Us ---
@router.put("/about", response_model=About)
async def update_about(about: AboutUpdate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    update_data = {k: v for k, v in about.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    await db["about"].update_one({}, {"$set": update_data}, upsert=True)
    updated_about = await db["about"].find_one()
    updated_about["_id"] = str(updated_about["_id"])
    return updated_about

# --- Achievements ---
@router.post("/achievements", response_model=Achievement)
async def create_achievement(item: AchievementCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    doc["created_at"] = datetime.utcnow()
    result = await db["achievements"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/achievements/{id}")
async def delete_achievement(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    await db["achievements"].delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

@router.put("/achievements/{id}", response_model=Achievement)
async def update_achievement(id: str, item: AchievementCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    await db["achievements"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    doc = await db["achievements"].find_one({"_id": ObjectId(id)})
    doc["_id"] = str(doc["_id"])
    return doc

# --- Services ---
@router.post("/services", response_model=Service)
async def create_service(item: ServiceCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    result = await db["services"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/services/{id}")
async def delete_service(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    await db["services"].delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

@router.put("/services/{id}", response_model=Service)
async def update_service(id: str, item: ServiceCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    update_data = item.model_dump()
    await db["services"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    doc = await db["services"].find_one({"_id": ObjectId(id)})
    doc["_id"] = str(doc["_id"])
    return doc

# --- Blogs ---
@router.post("/news", response_model=Blog)
async def create_blog(item: BlogCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    doc["created_at"] = datetime.utcnow()
    result = await db["news"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/news/{id}")
async def delete_blog(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    await db["news"].delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

@router.put("/news/{id}", response_model=Blog)
async def update_blog(id: str, item: BlogCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    await db["news"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    doc = await db["news"].find_one({"_id": ObjectId(id)})
    doc["_id"] = str(doc["_id"])
    return doc
