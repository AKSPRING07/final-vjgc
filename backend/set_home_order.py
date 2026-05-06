
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def set_order():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Setting order for Home Services...")
    services = [
        "IT Consulting",
        "Education & Training",
        "Healthcare & Wellness",
        "Export & Trading",
        "Business Consulting"
    ]
    
    for i, title in enumerate(services):
        await db["universal_content"].update_one(
            {"mainPage": "Home", "category": "Services", "title": title},
            {"$set": {"order": i}}
        )
        print(f"Set order {i} for {title}")

if __name__ == "__main__":
    asyncio.run(set_order())
