
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

async def migrate_data():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Migrating legacy services to universal_content...")
    
    async for doc in db["services"].find():
        # Check if it already exists in universal_content to avoid duplicates
        exists = await db["universal_content"].find_one({
            "mainPage": "Home",
            "category": "Services",
            "title": doc["title"]
        })
        
        if not exists:
            new_doc = {
                "mainPage": "Home",
                "subSection": "",
                "category": "Services",
                "title": doc.get("title", ""),
                "description": doc.get("description", ""),
                "image": doc.get("icon_url", doc.get("image_url", "/static/images/icon/icon_06.svg")),
                "isActive": True,
                "order": 0,
                "updatedAt": datetime.now()
            }
            await db["universal_content"].insert_one(new_doc)
            print(f"Migrated: {doc['title']}")
        else:
            print(f"Already exists: {doc['title']}")

if __name__ == "__main__":
    asyncio.run(migrate_data())
