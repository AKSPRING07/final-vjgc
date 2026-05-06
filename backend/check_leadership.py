import asyncio
from app.db.mongodb import connect_to_mongo, get_database

async def check():
    await connect_to_mongo()
    db = get_database()
    print("--- LEADERSHIP HERO CHECK ---")
    doc = await db['content'].find_one({'page': 'about', 'subpage': 'leadership', 'section': 'hero'})
    if doc:
        print(f"Status: {doc.get('status')}")
        print(f"Content: {doc.get('content')}")
    else:
        print("Not found")

if __name__ == "__main__":
    asyncio.run(check())
