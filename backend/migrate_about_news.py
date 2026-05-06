
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def migrate_news():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Migrating legacy news to universal_content (About -> Insights News)...")
    
    async for doc in db["news"].find():
        # Check if it already exists to avoid duplicates
        exists = await db["universal_content"].find_one({
            "mainPage": "About",
            "subSection": "About Group",
            "category": "Insights News",
            "title": doc["title"]
        })
        
        if not exists:
            new_doc = {
                "mainPage": "About",
                "subSection": "About Group",
                "category": "Insights News",
                "title": doc.get("title", ""),
                "description": doc.get("content", ""),
                "image": doc.get("image_url", ""),
                "author": doc.get("author", "Admin"),
                "category_name": "General", # to distinguish from CMS category
                "isActive": True,
                "order": 0,
                "updatedAt": datetime.now()
            }
            await db["universal_content"].insert_one(new_doc)
            print(f"Migrated: {doc['title']}")
        else:
            print(f"Already exists: {doc['title']}")

if __name__ == "__main__":
    asyncio.run(migrate_news())
