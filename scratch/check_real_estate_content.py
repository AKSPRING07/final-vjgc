import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load from backend/.env
load_dotenv('backend/.env')

async def check_db():
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DATABASE_NAME", "vjs_cms")
    
    print(f"Connecting to: {uri[:20]}...")
    print(f"Database: {db_name}")
    
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    collections = await db.list_collection_names()
    print(f"Collections: {collections}")
    
    if "content" not in collections:
        print("Error: 'content' collection not found!")
        return

    print("\nChecking 'content' collection for page='business', subpage='real-estate'...")
    cursor = db["content"].find({"page": "business", "subpage": "real-estate"})
    found = False
    async for doc in cursor:
        found = True
        print(f"Found: Section='{doc.get('section')}', Type='{doc.get('type')}', Status='{doc.get('status')}'")
        content = doc.get('content')
        print(f"  ContentType: {type(content)}")
        if isinstance(content, list):
            print(f"  List length: {len(content)}")
            if len(content) > 0:
                print(f"  First item keys: {content[0].keys()}")
        elif isinstance(content, dict):
            print(f"  Dict keys: {content.keys()}")
    
    if not found:
        print("No documents found for page='business', subpage='real-estate'")

if __name__ == "__main__":
    asyncio.run(check_db())
