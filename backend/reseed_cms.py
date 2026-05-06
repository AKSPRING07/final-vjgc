import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

async def reseed_cms():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    
    print("Clearing and reseeding business content with correct section names...")
    
    # Business subpages
    subpages = ["infrastructure", "energy", "transport", "consumer", "real-estate", "healthcare", "education", "hospitality", "technology", "finance"]
    
    for sub in subpages:
        # Hero
        hero = {
            "page": "business",
            "subpage": sub,
            "section": "hero",
            "type": "hero",
            "content": {
                "title": sub.replace("-", " ").title(),
                "subtitle": f"Leading excellence in {sub.replace('-', ' ')} solutions."
            },
            "status": "published",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        await db.content.update_one({"page": "business", "subpage": sub, "section": "hero"}, {"$set": hero}, upsert=True)
        
        # At a Glance
        glance = {
            "page": "business",
            "subpage": sub,
            "section": "at-a-glance",
            "type": "cards",
            "content": [
                {"_card_id": str(uuid.uuid4()), "title": "Innovation", "description": "Cutting edge technology solutions.", "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800"},
                {"_card_id": str(uuid.uuid4()), "title": "Quality", "description": "Highest standards of service delivery.", "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&q=80&w=800"}
            ],
            "status": "published",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        await db.content.update_one({"page": "business", "subpage": sub, "section": "at-a-glance"}, {"$set": glance}, upsert=True)
        
        # Our Business (This was previously named 'services' in some places, now fixed to 'our-business')
        our_biz = {
            "page": "business",
            "subpage": sub,
            "section": "our-business",
            "type": "cards",
            "content": [
                {"_card_id": str(uuid.uuid4()), "title": "Core Service A", "description": "Essential solution for your business.", "image_url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=800"},
                {"_card_id": str(uuid.uuid4()), "title": "Core Service B", "description": "Optimizing operations and growth.", "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800"}
            ],
            "status": "published",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        await db.content.update_one({"page": "business", "subpage": sub, "section": "our-business"}, {"$set": our_biz}, upsert=True)

    print("CMS content re-seeded successfully!")
    client.close()

if __name__ == "__main__":
    asyncio.run(reseed_cms())
