import asyncio
from app.db.mongodb import get_database

async def check():
    from app.db.mongodb import connect_to_mongo, get_database
    await connect_to_mongo()
    db = get_database()
    print("--- CONTENT CHECK ---")
    cursor = db['content'].find({'page': 'about'})
    async for doc in cursor:
        print(f"Page: {doc.get('page')}, Sub: {doc.get('subpage')}, Sec: {doc.get('section')}, Status: {doc.get('status')}")
    
    print("\n--- DASHBOARD CHECK ---")
    cursor = db['content'].find({'page': 'dashboard'})
    async for doc in cursor:
        print(f"Page: {doc.get('page')}, Sub: {doc.get('subpage')}, Sec: {doc.get('section')}, Status: {doc.get('status')}")

if __name__ == "__main__":
    asyncio.run(check())
