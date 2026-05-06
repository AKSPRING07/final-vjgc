import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

async def migrate_to_universal():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    
    print("Fetching legacy content...")
    legacy_cursor = db["content"].find({})
    
    universal_docs = []
    
    async for doc in legacy_cursor:
        page = doc.get("page", "unknown")
        subpage = doc.get("subpage", "General")
        section = doc.get("section", "General")
        content_type = doc.get("type", "text")
        content_data = doc.get("content", [])
        
        # Mapping technical names to friendly names if possible
        main_page = page.replace("-", " ").title()
        if main_page == "Business": main_page = "Business Verticals"
        
        sub_section = str(subpage).replace("-", " ").title()
        category = section.replace("-", " ").title()
        
        if isinstance(content_data, list):
            # It's a list of cards
            for idx, item in enumerate(content_data):
                universal_docs.append({
                    "mainPage": main_page,
                    "subSection": sub_section,
                    "category": category,
                    "title": item.get("title", ""),
                    "description": item.get("description", ""),
                    "image": item.get("image_url") or item.get("image", ""),
                    "order": idx,
                    "isActive": True,
                    "createdAt": datetime.utcnow()
                })
        elif isinstance(content_data, dict):
            # It's a single item (like a hero)
            universal_docs.append({
                "mainPage": main_page,
                "subSection": sub_section,
                "category": category,
                "title": content_data.get("title", ""),
                "description": content_data.get("subtitle") or content_data.get("description", ""),
                "image": content_data.get("image_url") or content_data.get("image", ""),
                "order": 0,
                "isActive": True,
                "createdAt": datetime.utcnow()
            })
            
    if universal_docs:
        print(f"Inserting {len(universal_docs)} items into universal_content...")
        # Clear existing first to avoid duplicates during migration testing
        await db["universal_content"].delete_many({})
        await db["universal_content"].insert_many(universal_docs)
        print("Migration successful!")
    else:
        print("No legacy content found to migrate.")
        
    client.close()

if __name__ == "__main__":
    asyncio.run(migrate_to_universal())
