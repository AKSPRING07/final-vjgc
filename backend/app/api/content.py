from fastapi import APIRouter, Depends, HTTPException, Query
from app.db.mongodb import get_database
from app.schemas.universal_content import UniversalContent, UniversalContentCreate, UniversalContentUpdate
from typing import List, Optional, Dict, Any
from datetime import datetime
from bson import ObjectId

router = APIRouter()

def serialize_doc(doc):
    if not doc: return None
    doc["id"] = str(doc.pop("_id"))
    return doc

@router.get("/", response_model=List[UniversalContent])
async def list_universal_content(
    mainPage: Optional[str] = Query(None),
    subSection: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    isActive: Optional[bool] = Query(None),
    db = Depends(get_database)
):
    print(f"--- FETCHING UNIVERSAL CONTENT ---")
    print(f"Params: mainPage={mainPage}, subSection={subSection}, category={category}")
    
    query = {}
    if mainPage:
        query["mainPage"] = mainPage
    if subSection:
        query["subSection"] = subSection
    if category:
        query["category"] = category
    if isActive is not None:
        query["isActive"] = isActive
        
    print(f"Executing Query: {query}")
    
    cursor = db["universal_content"].find(query).sort("order", 1)
    results = []
    async for doc in cursor:
        results.append(serialize_doc(doc))
    
    print(f"Results Found: {len(results)}")
    return results

@router.get("/all")
async def get_all_grouped(db = Depends(get_database)):
    """Returns all data grouped by mainPage -> subSection -> category"""
    pipeline = [
        {
            "$group": {
                "_id": {
                    "mainPage": "$mainPage",
                    "subSection": "$subSection",
                    "category": "$category"
                },
                "items": {
                    "$push": {
                        "id": {"$toString": "$_id"},
                        "title": "$title",
                        "description": "$description",
                        "image": "$image",
                        "order": "$order",
                        "isActive": "$isActive"
                    }
                }
            }
        }
    ]
    
    cursor = db["universal_content"].aggregate(pipeline)
    grouped = {}
    async for doc in cursor:
        m = doc["_id"]["mainPage"]
        s = doc["_id"]["subSection"]
        c = doc["_id"]["category"]
        
        if m not in grouped: grouped[m] = {}
        if s not in grouped[m]: grouped[m][s] = {}
        grouped[m][s][c] = doc["items"]
        
    return grouped

@router.post("/", response_model=UniversalContent)
async def create_universal_content(data: UniversalContentCreate, db = Depends(get_database)):
    print(f"--- CREATING UNIVERSAL CONTENT ---")
    print(f"Data: {data}")
    
    doc = data.model_dump()
    doc["createdAt"] = datetime.utcnow()
    
    result = await db["universal_content"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.put("/{id}", response_model=UniversalContent)
async def update_universal_content(id: str, data: UniversalContentUpdate, db = Depends(get_database)):
    print(f"--- UPDATING UNIVERSAL CONTENT ---")
    print(f"ID: {id}, Data: {data}")
    
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    
    result = await db["universal_content"].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": update_data},
        return_document=True
    )
    
    if not result:
        raise HTTPException(status_code=404, detail="Content not found")
        
    return serialize_doc(result)

@router.delete("/{id}")
async def delete_universal_content(id: str, db = Depends(get_database)):
    print(f"--- DELETING UNIVERSAL CONTENT ---")
    print(f"ID: {id}")
    
    result = await db["universal_content"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
        
    return {"message": "Content deleted successfully"}
