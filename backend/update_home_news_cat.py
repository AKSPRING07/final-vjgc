
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    r = await db["universal_content"].update_many(
        {"mainPage": "Home", "category": "Insights / News"},
        {"$set": {"category": "Insights News"}}
    )
    print(f"Updated {r.modified_count} items from Home")
    
    r = await db["universal_content"].update_many(
        {"mainPage": "Home", "category": "Insights / News"},
        {"$set": {"category": "Insights News"}}
    )
    # Just in case there are any left with the old name
    print("Migration complete.")

if __name__ == "__main__":
    asyncio.run(f())
