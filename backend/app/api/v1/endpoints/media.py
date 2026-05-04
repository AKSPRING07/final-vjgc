import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload an image and return its URL.
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Generate unique filename
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # In a real app, this would be a full URL
    # For local dev, we return the relative path or a constructed URL
    return {"url": f"/uploads/{unique_filename}", "filename": unique_filename}

@router.get("/list")
async def list_files():
    """
    List all uploaded images.
    """
    files = os.listdir(UPLOAD_DIR)
    return {"images": files}
