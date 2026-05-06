
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def find_duplicates():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    pipeline = [
        {"$group": {
            "_id": {"mainPage": "$mainPage", "subSection": "$subSection", "category": "$category", "title": "$title"},
            "count": {"$sum": 1},
            "ids": {"$push": "$_id"}
        }},
        {"$match": {"count": {"$gt": 1}}}
    ]
    
    print("Finding duplicates...")
    async for group in db["universal_content"].aggregate(pipeline):
        print(f"Duplicate group: {group['_id']}")
        # Keep the first one, delete the rest
        for doc_id in group["ids"][1:]:
            await db["universal_content"].delete_one({"_id": doc_id})
            print(f"Deleted duplicate ID: {doc_id}")

if __name__ == "__main__":
    asyncio.run(find_duplicates())
