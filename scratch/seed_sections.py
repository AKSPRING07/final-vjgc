import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('backend/.env')

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
        "infrastructure": [
            {"name": "hero", "type": "hero", "label": "Infrastructure Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "energy": [
            {"name": "hero", "type": "hero", "label": "Energy Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "transport": [
            {"name": "hero", "type": "hero", "label": "Transport Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "consumer": [
            {"name": "hero", "type": "hero", "label": "Consumer Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "real-estate": [
            {"name": "hero", "type": "hero", "label": "Real Estate Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "healthcare": [
            {"name": "hero", "type": "hero", "label": "Healthcare Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "education": [
            {"name": "hero", "type": "hero", "label": "Education Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "hospitality": [
            {"name": "hero", "type": "hero", "label": "Hospitality Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "technology": [
            {"name": "hero", "type": "hero", "label": "Technology Hero"}, 
            {"name": "at-a-glance", "type": "cards", "label": "At a Glance"},
            {"name": "our-business", "type": "cards", "label": "Our Business"}
        ],
        "finance": [
            {"name": "hero", "type": "hero", "label": "Finance Hero"}, 
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

async def seed():
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("DATABASE_NAME", "vjs_cms")]
    
    print("Seeding missing sections...")
    
    for page, config in PAGES_CONFIG.items():
        if isinstance(config, dict):
            for subpage, sections in config.items():
                for section in sections:
                    await ensure_section(db, page, subpage, section)
        else:
            for section in config:
                await ensure_section(db, page, None, section)
    
    print("Sync complete.")

async def ensure_section(db, page, subpage, section_config):
    name = section_config["name"]
    stype = section_config["type"]
    
    query = {"page": page, "section": name}
    if subpage:
        query["subpage"] = subpage
    else:
        query["$or"] = [{"subpage": None}, {"subpage": {"$exists": False}}, {"subpage": ""}]
        
    existing = await db["content"].find_one(query)
    
    if not existing:
        print(f"Creating missing section: {page} > {subpage if subpage else 'main'} > {name} ({stype})")
        doc = {
            "page": page,
            "subpage": subpage,
            "section": name,
            "type": stype,
            "content": [] if stype in ["cards", "news"] else {},
            "status": "published",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        await db["content"].insert_one(doc)
    else:
        # Check if type matches, and if cards/news, ensure content is a list
        update = {}
        if existing.get("type") != stype:
            print(f"Updating type for {page}/{subpage}/{name}: {existing.get('type')} -> {stype}")
            update["type"] = stype
            
        if stype in ["cards", "news"] and not isinstance(existing.get("content"), list):
            print(f"Converting content to list for {page}/{subpage}/{name}")
            update["content"] = []
            
        if update:
            await db["content"].update_one({"_id": existing["_id"]}, {"$set": update})

if __name__ == "__main__":
    asyncio.run(seed())
