from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.achievement import Achievement, AchievementCreate
from typing import List
from datetime import datetime
import uuid
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
MAX_FILE_SIZE = 5 * 1024 * 1024 # 5MB

@router.post("/media/upload")
async def upload_image(
    file: UploadFile = File(...),
    admin: str = Depends(get_current_admin)
):
    """
    Upload an image for the CMS. Protected by JWT.
    """
    # 1. Validate Extension
    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only JPG, JPEG, and PNG are allowed."
        )

    # 2. Generate Unique Filename
    unique_filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # 3. Save File
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Could not save file: {str(e)}"
        )

    return {
        "url": f"/uploads/{unique_filename}",
        "filename": unique_filename
    }

@router.get("/media/list")
async def list_media(admin: str = Depends(get_current_admin)):
    """List all uploaded media files."""
    files = os.listdir(UPLOAD_DIR)
    return {"images": files}

@router.post("/achievements", response_model=Achievement)
async def create_achievement(
    achievement: AchievementCreate, 
    db = Depends(get_database),
    admin = Depends(get_current_admin)
):
    """Admin API to create an achievement. Protected by JWT."""
    # Convert Pydantic model to dict
    new_achievement = achievement.model_dump()
    
    # Add timestamp
    new_achievement["created_at"] = datetime.utcnow()
    
    # Insert into MongoDB
    result = await db["achievements"].insert_one(new_achievement)
    
    # Add the generated ID back to the dict as a string
    new_achievement["_id"] = str(result.inserted_id)
    
    return new_achievement

@router.delete("/achievements/{id}")
async def delete_achievement(
    id: str, 
    db = Depends(get_database),
    admin = Depends(get_current_admin)
):
    """Admin API to delete an achievement."""
    result = await db["achievements"].delete_one({"_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return {"message": "Deleted successfully"}
