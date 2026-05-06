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
    "home":     "Home",
    "about":    "About",
    "business": "Business Verticals",
    "newsroom": "Newsroom",
    "blog":     "Blog",
    # Sub-sections (about)
    "about-group":  "About Group",
    "leadership":   "Leadership",
    "awards":       "Awards",
    "journey":      "Our Journey",
    # Sub-sections (newsroom)
    "media-release": "Media Release",
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
    "at-a-glance":    "At a Glance",
    "our-business":   "Our Business",
    "Hero Section":   "Hero Section",
    "Services":       "Services",
    "Insights / News": "Insights / News",
    "Advisors":       "Advisors",
    "Awards":         "Awards",
    "News":           "News",
}

def resolve(slug: Optional[str]) -> Optional[str]:
    """Translate a slug to its database-friendly name, or return as-is."""
    if slug is None:
        return None
    return SLUG_TO_NAME.get(slug, slug)

# --- Static Structure Configuration ---
# This defines the UI dropdowns in the Admin Panel.
PAGES_CONFIG = {
    "home": [
        {"name": "Hero Section",    "label": "Hero Section",    "type": "hero"},
        {"name": "Services",        "label": "Services",        "type": "cards"},
        {"name": "Insights / News", "label": "Insights / News", "type": "news"},
    ],
    "about": {
        "about-group": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "News Section", "label": "News Section", "type": "news"}
        ],
        "leadership": [
            {"name": "Advisors", "label": "Advisors", "type": "cards"}
        ],
        "awards": [
            {"name": "Awards", "label": "Awards", "type": "cards"}
        ]
    },
    "business": [
        {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
        {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
        {"name": "Our Business", "label": "Our Business", "type": "cards"}
    ],
    "newsroom": {
        "media-release": [
            {"name": "News", "label": "News", "type": "news"}
        ]
    },
    "blog": [
        {"name": "News", "label": "News", "type": "news"}
    ]
}


# ---------------------------------------------------------------------------
# GET /sections
# Called by Admin Panel when a page + sub-section is chosen.
# Returns the structural categories available to be edited.
# ---------------------------------------------------------------------------
@router.get("/sections")
async def get_sections(page: str = "home", subpage: Optional[str] = None):
    """Return the predefined categories for the selected page and subpage."""
    pk = page.lower()
    config = PAGES_CONFIG.get(pk)
    
    if config is None:
        return []
        
    # If the config for this page is a dictionary, it has subpages
    if isinstance(config, dict):
        # We must have a subpage to know what sections to return
        return config.get(subpage or "", [])
        
    # If it's a list, the page itself has the sections (no subpages, or all subpages share the same structure like 'business')
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

    # Infer section type from the category name so the admin renders correct fields
    hero_categories = {"Hero Section"}
    news_categories = {"Insights / News", "News Section", "News"}
    if c in hero_categories:
        section_type = "hero"
    elif c in news_categories:
        section_type = "news"
    else:
        section_type = "cards"

    return {
        "content": results,
        "type":    section_type,
        "id":      f"{m}-{s}-{c}"
    }


# ---------------------------------------------------------------------------
# PUT /content  (upsert a single item)
# ---------------------------------------------------------------------------
@router.put("/content")
async def upsert_content(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    mainPage   = resolve(data.get("mainPage"))
    subSection = resolve(data.get("subSection")) or ""   # Optional for Home/Blog
    category   = resolve(data.get("category"))

    if not all([mainPage, category]):
        raise HTTPException(status_code=400, detail="mainPage and category are required")

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
