import asyncio
from app.db.mongodb import connect_to_mongo, get_database

async def check():
    await connect_to_mongo()
    db = get_database()
    print("--- BUSINESS CONTENT CHECK ---")
    async for doc in db['content'].find({'page': 'business'}):
        print(f"Subpage: {doc.get('subpage')} | Section: {doc.get('section')} | Type: {doc.get('type')} | Content Type: {type(doc.get('content'))}")
    
    print("\n--- ALL SECTIONS LIST ---")
    async for doc in db['content'].find():
        print(f"ID: {doc['_id']} | Page: {doc['page']} | Subpage: {doc.get('subpage')} | Section: {doc['section']}")

if __name__ == "__main__":
    asyncio.run(check())
