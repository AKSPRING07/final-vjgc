
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- ALL UNIVERSAL CONTENT ---")
    async for d in db["universal_content"].find():
        print(f"P: {d.get('mainPage')} | S: {d.get('subSection')} | C: {d.get('category')} | T: {d.get('title')}")

if __name__ == "__main__":
    asyncio.run(f())
