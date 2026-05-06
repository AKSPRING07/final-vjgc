import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check():
    client = AsyncIOMotorClient("mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0")
    db = client["vjs_cms"]
    docs = await db["content"].find({"page": "business"}).to_list(None)
    for d in docs:
        print(f"Subpage: {d.get('subpage')}, Section: {d.get('section')}, ID: {d.get('_id')}")

asyncio.run(check())
