from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_helper = MongoDB()

async def connect_to_mongo():
    db_helper.client = AsyncIOMotorClient(settings.MONGO_URI)
    db_helper.db = db_helper.client[settings.DATABASE_NAME]
    print("Connected to MongoDB Atlas")

async def close_mongo_connection():
    db_helper.client.close()
    print("Closed MongoDB connection")

def get_database():
    return db_helper.db
