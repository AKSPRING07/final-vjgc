from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.content import Content, ContentCreate, ContentUpdate
from typing import List, Dict, Any, Optional
from datetime import datetime
from bson import ObjectId
import uuid

router = APIRouter()

# --- Section Configuration ---
PAGES_CONFIG = {
    "home": [
        {"name": "hero", "type": "hero", "label": "Main Hero Section"},
        {"name": "features", "type": "cards", "label": "Core Features"},
    ],
    "about": {
        "about-group": [
            {"name": "hero", "type": "hero", "label": "About Hero"},
            {"name": "content", "type": "text", "label": "About Content"}
        ],
        "journey": [
            {"name": "hero", "type": "hero", "label": "Journey Hero"},
            {"name": "timeline", "type": "cards", "label": "Journey Timeline"}
        ],
        "leadership": [
            {"name": "hero", "type": "hero", "label": "Leadership Hero"},
            {"name": "team", "type": "cards", "label": "Leadership Team"}
        ],
        "awards": [
            {"name": "hero", "type": "hero", "label": "Awards Hero"},
            {"name": "award_list", "type": "cards", "label": "Award List"}
        ]
    },
    "business": {
        "it-consulting": [
            {"name": "hero", "type": "hero", "label": "IT Consulting Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "data-centers": [
            {"name": "hero", "type": "hero", "label": "Data Centers Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "export-import": [
            {"name": "hero", "type": "hero", "label": "Export & Import Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "plantations": [
            {"name": "hero", "type": "hero", "label": "Plantations Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "it-training": [
            {"name": "hero", "type": "hero", "label": "IT Training Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "yoga-wellness": [
            {"name": "hero", "type": "hero", "label": "Yoga & Wellness Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "property-services": [
            {"name": "hero", "type": "hero", "label": "Property Services Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "green-energy": [
            {"name": "hero", "type": "hero", "label": "Green Energy Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "logistics": [
            {"name": "hero", "type": "hero", "label": "Logistics Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "travel-rentals": [
            {"name": "hero", "type": "hero", "label": "Travel & Rentals Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ]
    },
    "newsroom": {
        "media-release": [
            {"name": "hero", "type": "hero", "label": "Media Release Hero"},
            {"name": "releases", "type": "news", "label": "Media Releases"}
        ]
    },
    "blog": [
        {"name": "hero", "type": "hero", "label": "Blog Hero"},
        {"name": "posts", "type": "cards", "label": "Blog Posts"},
    ]
}

@router.get("/sections") 
async def get_sections(page: str = "home", subpage: Optional[str] = None):
    page_key = page.lower()
    if page_key not in PAGES_CONFIG:
        return []
    
    config = PAGES_CONFIG[page_key]
    
    if isinstance(config, dict):
        if not subpage or subpage not in config:
            return []
        return config[subpage]
    
    return config


@router.get("/content")
async def get_content(
    page: Optional[str] = None, 
    section: Optional[str] = None, 
    subpage: Optional[str] = None, 
    mainPage: Optional[str] = None, 
    subSection: Optional[str] = None, 
    category: Optional[str] = None,
    status: Optional[str] = None, 
    db = Depends(get_database)
):
    # Mapping aliases
    page = page or mainPage
    if page == "Business Verticals": page = "business"
    subpage = subpage or subSection
    section = section or category
    if section == "Our Business": section = "our-business"

    print(f"DEBUG: Fetching content for Page={page}, Subpage={subpage}, Section={section}")
    
    query = {}
    if page:
        query["page"] = page.lower()
    
    if subpage:
        query["subpage"] = subpage.lower()
    else:
        query["$or"] = [{"subpage": None}, {"subpage": {"$exists": False}}, {"subpage": ""}]
    
    if section:
        query["section"] = section.lower()
        print(f"DEBUG: Executing find_one with query: {query}")
        doc = await db["content"].find_one(query)
        if doc:
            doc["_id"] = str(doc["_id"])
            # Ensure content is a list for cards/news if it's currently a dict or None
            if doc.get("type") in ["cards", "news"] and not isinstance(doc.get("content"), list):
                doc["content"] = []
        return doc
    
    if status:
        query["status"] = status
        
    docs = []
    print(f"DEBUG: Executing find with query: {query}")
    async for doc in db["content"].find(query):
        doc["_id"] = str(doc["_id"])
        if doc.get("type") in ["cards", "news"] and not isinstance(doc.get("content"), list):
            doc["content"] = []
        docs.append(doc)
    return docs

@router.put("/content", response_model=Content)
async def upsert_content(item: ContentCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    
    subpage = item.subpage if item.subpage else None
    query = {"page": item.page, "section": item.section}
    if subpage:
        query["subpage"] = subpage
    else:
        query["$or"] = [{"subpage": None}, {"subpage": {"$exists": False}}, {"subpage": ""}]

    existing = await db["content"].find_one(query)
    
    # Handle Granular Card Actions
    action = update_data.get("action")
    card_id = update_data.get("card_id")
    card_data = update_data.get("data")

    if existing:
        # Save current content to versions before updating
        version_entry = {
            "content": existing["content"],
            "updated_at": existing.get("updated_at", existing.get("created_at")),
            "status": existing.get("status")
        }
        
        # Clean up data for update
        update_data.pop("versions", None)
        update_data.pop("_id", None)
        update_data.pop("created_at", None)
        update_data.pop("action", None)
        update_data.pop("card_id", None)
        update_data.pop("data", None)

        if action == "create_card":
            # Add a new card with a generated ID
            new_card = card_data
            if "_card_id" not in new_card:
                new_card["_card_id"] = str(uuid.uuid4())
            
            # ENSURE content is an array if we are pushing to it
            if not isinstance(existing.get("content"), list):
                await db["content"].update_one({"_id": existing["_id"]}, {"$set": {"content": []}})

            await db["content"].update_one(
                {"_id": existing["_id"]},
                {
                    "$push": {"content": new_card, "versions": {"$each": [version_entry], "$slice": -5}},
                    "$set": {"updated_at": datetime.utcnow()}
                }
            )
        elif action == "update_card" and card_id:
            # Update a specific card in the list
            await db["content"].update_one(
                {"_id": existing["_id"], "content._card_id": card_id},
                {
                    "$set": {"content.$": {**card_data, "_card_id": card_id}, "updated_at": datetime.utcnow()},
                    "$push": {"versions": {"$each": [version_entry], "$slice": -5}}
                }
            )
        elif action == "delete_card" and card_id:
            # Remove a specific card from the list
            await db["content"].update_one(
                {"_id": existing["_id"]},
                {
                    "$pull": {"content": {"_card_id": card_id}},
                    "$set": {"updated_at": datetime.utcnow()},
                    "$push": {"versions": {"$each": [version_entry], "$slice": -5}}
                }
            )
        else:
            # Standard full update
            await db["content"].update_one(
                {"_id": existing["_id"]},
                {
                    "$set": update_data,
                    "$push": {
                        "versions": {
                            "$each": [version_entry],
                            "$slice": -5
                        }
                    }
                }
            )
        update_data["_id"] = str(existing["_id"])
    return update_data

# Direct Card Addition API as requested
@router.post("/content")
async def add_single_card(card_request: Dict[str, Any], db = Depends(get_database)):
    main_page = card_request.get("mainPage", "business")
    if main_page == "Business Verticals": main_page = "business"
    sub_section = card_request.get("subSection", "travel").lower()
    category = card_request.get("category", "our-business").lower()
    if category == "our business": category = "our-business"

    print(f"DEBUG: Adding single card to Page={main_page}, Subpage={sub_section}, Section={category}")

    # Find the container document
    query = {"page": main_page, "subpage": sub_section, "section": category}
    existing = await db["content"].find_one(query)

    new_card = {
        "_card_id": str(uuid.uuid4()),
        "title": card_request.get("title"),
        "description": card_request.get("description"),
        "image_url": card_request.get("image") or card_request.get("image_url")
    }

    if existing:
        await db["content"].update_one(
            {"_id": existing["_id"]},
            {"$push": {"content": new_card}, "$set": {"updated_at": datetime.utcnow()}}
        )
        return {"message": "Card added to existing section", "card": new_card}
    else:
        # Create new section if it doesn't exist
        new_doc = {
            "page": main_page,
            "subpage": sub_section,
            "section": category,
            "type": "cards",
            "content": [new_card],
            "status": "published",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = await db["content"].insert_one(new_doc)
        return {"message": "Created new section and added card", "card": new_card}

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


@router.post("/content/{id}/card")
async def add_card(id: str, card_data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    if "_card_id" not in card_data:
        card_data["_card_id"] = str(uuid.uuid4())
    
    result = await db["content"].update_one(
        {"_id": ObjectId(id)},
        {"$push": {"content": card_data}, "$set": {"updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Content container not found")
    return card_data


@router.put("/content/{id}/card/{card_id}")
async def update_card(id: str, card_id: str, card_data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["content"].update_one(
        {"_id": ObjectId(id), "content._card_id": card_id},
        {"$set": {"content.$": {**card_data, "_card_id": card_id}, "updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Card or Container not found")
    return card_data


@router.delete("/content/{id}/card/{card_id}")
async def delete_card(id: str, card_id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["content"].update_one(
        {"_id": ObjectId(id)},
        {"$pull": {"content": {"_card_id": card_id}}, "$set": {"updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Card or Container not found")
    return {"message": "Card deleted"}

@router.post("/content/{id}/undo")
async def undo_content(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = await db["content"].find_one({"_id": ObjectId(id)})
    if not doc or "versions" not in doc or not doc["versions"]:
        raise HTTPException(status_code=404, detail="No previous versions found")
    
    # Get the last version
    versions = doc["versions"]
    previous_version = versions.pop()
    
    # Restore it
    await db["content"].update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "content": previous_version["content"],
            "updated_at": datetime.utcnow(),
            "versions": versions
        }}
    )
    
    restored = await db["content"].find_one({"_id": ObjectId(id)})
    restored["_id"] = str(restored["_id"])
    return restored

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

@router.post("/init-content")
async def init_content(db = Depends(get_database), admin: str = Depends(get_current_admin)):
    # --- 1. HOME PAGE ---
    # Home Hero
    home_hero = {
        "page": "home",
        "subpage": None,
        "section": "hero",
        "type": "hero",
        "content": {
            "title": "Vijayalakshmi Group Of Companies",
            "subtitle": "Engineering a sustainable future through innovation and integrity.",
            "video_url": "/static/images/hero video/hero-video.mp4",
            "cta_text": "Explore Our Journey"
        },
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "home", "section": "hero", "subpage": None}, {"$set": home_hero}, upsert=True)
    
    # Home Services (Cards)
    services_cards = [
        {"_card_id": str(uuid.uuid4()), "title": "IT Infrastructure", "description": "Enterprise-grade data centers and hosting solutions for global businesses.", "icon_url": "/static/images/icon/it_infra.png"},
        {"_card_id": str(uuid.uuid4()), "title": "Energy & Sustainability", "description": "Pioneering green energy and solar manufacturing for a cleaner tomorrow.", "icon_url": "/static/images/icon/energy.png"},
        {"_card_id": str(uuid.uuid4()), "title": "Agri & Trade", "description": "Global export-import operations and sustainable plantation management.", "icon_url": "/static/images/icon/agri.png"},
        {"_card_id": str(uuid.uuid4()), "title": "Real Estate", "description": "Premium property development and strategic real estate services.", "icon_url": "/static/images/icon/real_estate.png"},
        {"_card_id": str(uuid.uuid4()), "title": "Healthcare", "description": "Innovating in health sciences and wellness for better community care.", "icon_url": "/static/images/icon/healthcare.png"},
        {"_card_id": str(uuid.uuid4()), "title": "Education", "description": "Skill development and academic excellence for the next generation.", "icon_url": "/static/images/icon/education.png"}
    ]
    home_features = {
        "page": "home",
        "subpage": None,
        "section": "features",
        "type": "cards",
        "content": services_cards,
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "home", "section": "features", "subpage": None}, {"$set": home_features}, upsert=True)

    # --- 2. ABOUT US -> ABOUT GROUP ---
    about_hero = {
        "page": "about",
        "subpage": "about-group",
        "section": "hero",
        "type": "hero",
        "content": {
            "title": "About Vijayalakshmi Group",
            "subtitle": "Empowering the future through diversified industrial excellence and sustainable innovation.",
            "image_url": "/static/images/media/about_hero_cinematic.png"
        },
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "about", "subpage": "about-group", "section": "hero"}, {"$set": about_hero}, upsert=True)

    about_content = {
        "page": "about",
        "subpage": "about-group",
        "section": "content",
        "type": "text",
        "content": {
            "title": "Our Corporate Profile",
            "subtitle": "Decades of Trust & Excellence",
            "content": "Vijayalakshmi Group is a global conglomerate with a footprint across multiple sectors including IT, Energy, Agri-trade, and Real Estate. We are committed to building a sustainable future through innovation, integrity, and social responsibility.",
            "author": "Vijayalakshmi Group",
            "role": "Corporate Statement"
        },
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "about", "subpage": "about-group", "section": "content"}, {"$set": about_content}, upsert=True)

    # --- 3. BUSINESSES -> INFRASTRUCTURE ---
    infra_hero = {
        "page": "business",
        "subpage": "infrastructure",
        "section": "hero",
        "type": "hero",
        "content": {
            "title": "IT Infrastructure",
            "subtitle": "Building the digital backbone of modern enterprises.",
            "image_url": "/static/images/media/infra_hero.jpg"
        },
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "business", "subpage": "infrastructure", "section": "hero"}, {"$set": infra_hero}, upsert=True)

    # --- 4. BUSINESS VERTICALS ---
    for biz in ["infrastructure", "energy", "transport", "consumer", "real-estate", "healthcare", "education", "hospitality", "technology", "finance"]:
        # Business Hero
        biz_hero = {
            "page": "business",
            "subpage": biz,
            "section": "hero",
            "type": "hero",
            "content": {"title": biz.replace("-", " ").title(), "subtitle": f"Leading the way in {biz.replace('-', ' ')}."},
            "status": "published",
            "created_at": datetime.utcnow()
        }
        await db["content"].update_one({"page": "business", "subpage": biz, "section": "hero"}, {"$set": biz_hero}, upsert=True)
        
        # Business At a Glance (Cards)
        biz_glance = {
            "page": "business",
            "subpage": biz,
            "section": "at-a-glance",
            "type": "cards",
            "content": [],
            "status": "published",
            "created_at": datetime.utcnow()
        }
        await db["content"].update_one({"page": "business", "subpage": biz, "section": "at-a-glance"}, {"$set": biz_glance}, upsert=True)
        
        # Business Our Business (Cards)
        biz_main = {
            "page": "business",
            "subpage": biz,
            "section": "our-business",
            "type": "cards",
            "content": [],
            "status": "published",
            "created_at": datetime.utcnow()
        }
        await db["content"].update_one({"page": "business", "subpage": biz, "section": "our-business"}, {"$set": biz_main}, upsert=True)

    # --- 5. NEWSROOM -> MEDIA RELEASE ---
    news_items = [
        {
            "_card_id": str(uuid.uuid4()),
            "title": "VJS Group Announces Global Sustainability Initiative",
            "author": "Corporate Media Team",
            "date": "May 15, 2026",
            "image_url": "/static/images/blog/blog_01.jpg",
            "description": "The group has pledged to achieve net-zero carbon emissions across all its industrial facilities by 2040."
        },
        {
            "_card_id": str(uuid.uuid4()),
            "title": "Expansion into New Digital Transformation Markets",
            "author": "Market Analysis Desk",
            "date": "April 20, 2026",
            "image_url": "/static/images/blog/blog_02.jpg",
            "description": "VJS IT Infrastructure division is expanding its footprint into Southeast Asian markets with new data centers."
        }
    ]
    media_releases = {
        "page": "newsroom",
        "subpage": "media-release",
        "section": "releases",
        "type": "news",
        "content": news_items,
        "status": "published",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await db["content"].update_one({"page": "newsroom", "subpage": "media-release", "section": "releases"}, {"$set": media_releases}, upsert=True)
    
    return {"message": "All hardcoded frontend content successfully migrated to VJS Cloud CMS."}
