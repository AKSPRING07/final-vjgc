
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os

async def check_data():
    # Load from .env if needed, but I'll hardcode for this check
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- Services Collection ---")
    try:
        async for doc in db["services"].find():
            print(doc)
    except Exception as e:
        print(f"Error fetching services: {e}")
        
    print("\n--- Universal Content (Home Services) ---")
    try:
        # Check both "Services" and "Our Business" for Home page
        async for doc in db["universal_content"].find({"mainPage": "Home", "category": {"$in": ["Services", "Our Business"]}}):
            print(f"Cat: {doc.get('category')}, Title: {doc.get('title')}, Active: {doc.get('isActive')}")
    except Exception as e:
        print(f"Error fetching universal_content home: {e}")

    print("\n--- Universal Content (All Sections for Home) ---")
    try:
        async for doc in db["universal_content"].find({"mainPage": "Home"}):
            print(f"Sub: {doc.get('subSection')}, Cat: {doc.get('category')}, Title: {doc.get('title')}")
    except Exception as e:
        print(f"Error fetching universal_content all: {e}")

if __name__ == "__main__":
    asyncio.run(check_data())
