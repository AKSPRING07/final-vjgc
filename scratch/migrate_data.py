import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv('backend/.env')

async def migrate():
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("DATABASE_NAME", "vjs_cms")]
    
    # Rename 'services' to 'our-business'
    res = await db['content'].update_many({'section': 'services'}, {'$set': {'section': 'our-business'}})
    print(f"Renamed {res.modified_count} 'services' sections to 'our-business'")
    
    # Check for any 'cards' or 'news' sections where content is not a list
    cursor = db['content'].find({'type': {'$in': ['cards', 'news']}})
    async for doc in cursor:
        if not isinstance(doc.get('content'), list):
            print(f"Fixing content structure for {doc.get('page')}/{doc.get('subpage')}/{doc.get('section')}")
            # If it's a dict with 'items' key, use that
            new_content = []
            if isinstance(doc.get('content'), dict) and 'items' in doc.get('content'):
                new_content = doc['content']['items']
                print(f"  Extracted {len(new_content)} items from dict['items']")
            
            await db['content'].update_one({'_id': doc['_id']}, {'$set': {'content': new_content}})

if __name__ == "__main__":
    asyncio.run(migrate())
