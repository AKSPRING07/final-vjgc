
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def fix_home_subsection():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Fixing Home subSection (space to empty string)...")
    # Update all items for Home page
    r = await db["universal_content"].update_many(
        {"mainPage": "Home", "subSection": " "},
        {"$set": {"subSection": ""}}
    )
    print(f"Updated {r.modified_count} items.")

if __name__ == "__main__":
    asyncio.run(fix_home_subsection())
