import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv('backend/.env')

async def check_db():
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DATABASE_NAME", "vjs_cms")
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print(f"Sections for page='business', subpage='real-estate':")
    cursor = db["content"].find({"page": "business", "subpage": "real-estate"})
    async for doc in cursor:
        print(f"- {doc.get('section')} ({doc.get('type')})")
        
    print(f"\nSections for page='business', subpage='infrastructure':")
    cursor = db["content"].find({"page": "business", "subpage": "infrastructure"})
    async for doc in cursor:
        print(f"- {doc.get('section')} ({doc.get('type')})")

if __name__ == "__main__":
    asyncio.run(check_db())
