
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- HOME NEWS ACTIVE STATUS ---")
    async for d in db["universal_content"].find({"mainPage": "Home", "category": "Insights News"}):
        print(f"Title: {d.get('title')} | Active: {d.get('isActive')}")

if __name__ == "__main__":
    asyncio.run(f())
