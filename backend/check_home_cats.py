
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- HOME CONTENT CATEGORIES ---")
    async for d in db["universal_content"].find({"mainPage": "Home"}):
        print(f"Title: {d.get('title')} | Cat: {repr(d.get('category'))}")

if __name__ == "__main__":
    asyncio.run(f())
