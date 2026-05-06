from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.universal_content import UniversalContent, UniversalContentCreate, UniversalContentUpdate
from typing import List, Dict, Any, Optional
from datetime import datetime
from bson import ObjectId
import uuid

router = APIRouter()

# Mapping: slug sent by admin panel → friendly name stored in MongoDB
SLUG_TO_NAME = {
    # Main pages
    "business": "Business Verticals",
    # Sub-sections (business verticals)
    "it-consulting":      "IT Consulting",
    "data-centers":       "Enterprise Data Centers & Hosting Services",
    "export-import":      "Export & Import",
    "plantations":        "Plantations & Exotic Trees",
    "it-training":        "IT Training",
    "yoga-wellness":      "Yoga & Wellness",
    "property-services":  "Property Services",
    "green-energy":       "Green Energy & Solar Manufacturing",
    "logistics":          "Logistics Services",
    "travel-rentals":     "Travel & Rentals",
    # Categories
    "at-a-glance":   "At a Glance",
    "our-business":  "Our Business",
}

def resolve(slug: Optional[str]) -> Optional[str]:
    """Translate a slug to its database-friendly name, or return as-is."""
    if slug is None:
        return None
    return SLUG_TO_NAME.get(slug, slug)

# --- Static config for the ABOUT / HOME fallback (business is now fully dynamic) ---
PAGES_CONFIG = {
    "home": [
        {"name": "hero",     "type": "hero",  "label": "Main Hero Section"},
        {"name": "features", "type": "cards", "label": "Core Features"},
    ],
    "about": {
        "about-group": [
            {"name": "hero",    "type": "hero", "label": "About Hero"},
            {"name": "content", "type": "text", "label": "About Content"}
        ],
        "journey": [
            {"name": "hero",     "type": "hero",  "label": "Journey Hero"},
            {"name": "timeline", "type": "cards", "label": "Journey Timeline"}
        ],
        "leadership": [
            {"name": "hero", "type": "hero",  "label": "Leadership Hero"},
            {"name": "team", "type": "cards", "label": "Leadership Team"}
        ],
        "awards": [
            {"name": "hero",       "type": "hero",  "label": "Awards Hero"},
            {"name": "award_list", "type": "cards", "label": "Award List"}
        ]
    }
}


# ---------------------------------------------------------------------------
# GET /sections
# Called by Admin Panel when a page + sub-section is chosen.
# Returns the categories available for that sub-section.
# ---------------------------------------------------------------------------
@router.get("/sections")
async def get_sections(page: str = "home", subpage: Optional[str] = None, db = Depends(get_database)):
    """Dynamically return categories by querying existing DB content."""

    # Translate slugs → DB names
    db_page    = resolve(page)    # "business" → "Business Verticals"
    db_subpage = resolve(subpage) # "travel-rentals" → "Travel & Rentals"

    print(f"DEBUG /sections: page={page}→{db_page}, subpage={subpage}→{db_subpage}")

    query: Dict[str, Any] = {"mainPage": db_page}
    if db_subpage:
        query["subSection"] = db_subpage

    pipeline = [{"$match": query}, {"$group": {"_id": "$category"}}]
    existing = []
    async for doc in db["universal_content"].aggregate(pipeline):
        cat = doc["_id"]
        if cat:
            existing.append({"name": cat, "label": cat, "type": "cards"})

    print(f"DEBUG /sections result: {existing}")

    if existing:
        return existing

    # Fallback to static config (used for home/about which aren't in universal_content)
    pk = page.lower()
    config = PAGES_CONFIG.get(pk)
    if config is None:
        return []
    if isinstance(config, dict):
        return config.get(subpage or "", [])
    return config


# ---------------------------------------------------------------------------
# GET /content
# Called to load cards for the selected category.
# ---------------------------------------------------------------------------
@router.get("/content")
async def get_content(
    page:      Optional[str] = None,
    subpage:   Optional[str] = None,
    section:   Optional[str] = None,
    mainPage:  Optional[str] = None,
    subSection: Optional[str] = None,
    category:  Optional[str] = None,
    db = Depends(get_database)
):
    m = resolve(page or mainPage)
    s = resolve(subpage or subSection)
    c = resolve(section or category)

    print(f"DEBUG /content: m={m}, s={s}, c={c}")

    # --- List-all mode (used by Product List explorer) ---
    if not m and not s and not c:
        pipeline = [
            {"$group": {
                "_id": {"mainPage": "$mainPage", "subSection": "$subSection", "category": "$category"},
                "count":         {"$sum": 1},
                "last_modified": {"$max": "$updatedAt"},
                "is_active":     {"$first": "$isActive"}
            }}
        ]
        sections = []
        async for doc in db["universal_content"].aggregate(pipeline):
            sections.append({
                "_id":        f"{doc['_id']['mainPage']}-{doc['_id']['subSection']}-{doc['_id']['category']}",
                "page":       doc["_id"]["mainPage"],
                "subpage":    doc["_id"]["subSection"],
                "section":    doc["_id"]["category"],
                "status":     "published" if doc.get("is_active") else "draft",
                "type":       "cards",
                "updated_at": doc.get("last_modified"),
                "count":      doc["count"]
            })
        return sections

    # --- Specific content fetch ---
    query: Dict[str, Any] = {}
    if m: query["mainPage"]  = m
    if s: query["subSection"] = s
    if c: query["category"]  = c

    results = []
    async for doc in db["universal_content"].find(query).sort("order", 1):
        doc["_id"] = str(doc.pop("_id"))
        results.append(doc)

    print(f"DEBUG /content found {len(results)} items")

    return {
        "content": results,
        "type":    "cards",
        "id":      f"{m}-{s}-{c}"
    }


# ---------------------------------------------------------------------------
# PUT /content  (upsert a single item)
# ---------------------------------------------------------------------------
@router.put("/content")
async def upsert_content(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    mainPage   = resolve(data.get("mainPage"))
    subSection = resolve(data.get("subSection"))
    category   = resolve(data.get("category"))

    if not all([mainPage, subSection, category]):
        raise HTTPException(status_code=400, detail="mainPage, subSection and category are required")

    doc = {
        "mainPage":   mainPage,
        "subSection": subSection,
        "category":   category,
        "title":      data.get("title", "Section Content"),
        "description": data.get("description", ""),
        "image":      data.get("image", ""),
        "updatedAt":  datetime.utcnow(),
        "isActive":   True,
        "order":      data.get("order", 0)
    }

    await db["universal_content"].update_one(
        {"mainPage": mainPage, "subSection": subSection, "category": category, "title": doc["title"]},
        {"$set": doc, "$setOnInsert": {"createdAt": datetime.utcnow()}},
        upsert=True
    )
    return {"message": "Success"}


# ---------------------------------------------------------------------------
# POST /content  (upsert alias for the "Add to Collection" button)
# ---------------------------------------------------------------------------
@router.post("/content")
async def create_content(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    """Upsert a single content item."""
    return await upsert_content(data, db, admin)


# ---------------------------------------------------------------------------
# PUT /content/{id}  (update by MongoDB _id)
# ---------------------------------------------------------------------------
@router.put("/content/{id}")
async def update_content_by_id(id: str, data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    data.pop("_id", None)
    data["updatedAt"] = datetime.utcnow()
    
    # Ensure any slugs sent by the frontend are resolved back to DB friendly names
    if "mainPage" in data:   data["mainPage"]   = resolve(data["mainPage"])
    if "subSection" in data: data["subSection"] = resolve(data["subSection"])
    if "category" in data:   data["category"]   = resolve(data["category"])
        
    result = await db["universal_content"].update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Updated"}


# ---------------------------------------------------------------------------
# DELETE /content/{id}
# ---------------------------------------------------------------------------
@router.delete("/content/{id}")
async def delete_content(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["universal_content"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Deleted"}
