
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- NEWS COLLECTION ---")
    async for d in db["news"].find():
        print(d)

if __name__ == "__main__":
    asyncio.run(f())
