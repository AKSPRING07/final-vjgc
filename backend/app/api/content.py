from fastapi import APIRouter, Depends, HTTPException, Query
from app.db.mongodb import get_database
from app.schemas.content import Content, ContentCreate, ContentUpdate
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

router = APIRouter()

def serialize_doc(doc):
    doc["id"] = str(doc.pop("_id"))
    return doc

@router.get("/", response_model=List[Content])
async def list_content(
    status: Optional[str] = Query(None),
    db = Depends(get_database)
):
    query = {}
    if status:
        query["status"] = status
    
    cursor = db["content"].find(query).sort("created_at", -1)
    contents = []
    async for doc in cursor:
        contents.append(serialize_doc(doc))
    return contents

@router.post("/", response_model=Content)
async def create_content(content: ContentCreate, db = Depends(get_database)):
    doc = content.model_dump()
    doc["created_at"] = datetime.utcnow()
    doc["updated_at"] = datetime.utcnow()
    
    result = await db["content"].insert_one(doc)
    doc["id"] = str(result.inserted_id)
    return doc

@router.put("/{id}", response_model=Content)
async def update_content(id: str, content: ContentUpdate, db = Depends(get_database)):
    update_data = {k: v for k, v in content.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    result = await db["content"].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": update_data},
        return_document=True
    )
    
    if not result:
        raise HTTPException(status_code=404, detail="Content not found")
    
    return serialize_doc(result)

@router.put("/{id}/publish", response_model=Content)
async def publish_content(id: str, db = Depends(get_database)):
    result = await db["content"].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {"status": "published", "updated_at": datetime.utcnow()}},
        return_document=True
    )
    
    if not result:
        raise HTTPException(status_code=404, detail="Content not found")
    
    return serialize_doc(result)

@router.delete("/{id}")
async def delete_content(id: str, db = Depends(get_database)):
    result = await db["content"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Content deleted successfully"}
