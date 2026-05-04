import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_connection():
    uri = os.getenv("MONGO_URI")
    print(f"Connecting to: {uri[:20]}...")
    
    try:
        client = AsyncIOMotorClient(uri)
        # The is_master command is cheap and does not require auth.
        await client.admin.command('ismaster')
        print("[SUCCESS] Successfully connected to MongoDB Atlas!")
        
        # List databases to confirm access
        dbs = await client.list_database_names()
        print(f"Available Databases: {dbs}")
        
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(test_connection())
