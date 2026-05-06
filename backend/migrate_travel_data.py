import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

async def migrate_travel_data():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    
    # Data from travel-rentals.html
    # At a Glance
    at_a_glance_cards = [
        {"_card_id": str(uuid.uuid4()), "title": "Lakshmi Travels", "description": "Tourism & Rentals: Providing premium and reliable travel experiences.", "image_url": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=1000"},
        {"_card_id": str(uuid.uuid4()), "title": "Strategic Positioning", "description": "Leading the market through optimized routes and customer-centric travel hubs.", "image_url": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&q=80&w=1000"},
        {"_card_id": str(uuid.uuid4()), "title": "Vertical Integration", "description": "Enables seamless flow across trade, tourism, and supply chain networks.", "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=1000"}
    ]
    
    # Our Travel Businesses
    our_travel_businesses = [
        {"_card_id": str(uuid.uuid4()), "title": "Tour Packages", "description": "Customized travel experiences for leisure and group tourism.", "image_url": "https://images.unsplash.com/photo-1503220317375-aaad61436b1b?auto=format&fit=crop&q=80&w=1000"},
        {"_card_id": str(uuid.uuid4()), "title": "Vehicle Rentals", "description": "Flexible rental services for cars, vans, and utility vehicles.", "image_url": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=1000"},
        {"_card_id": str(uuid.uuid4()), "title": "Corporate Travel", "description": "End-to-end travel management for business and enterprise clients.", "image_url": "https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?auto=format&fit=crop&q=80&w=800"},
        {"_card_id": str(uuid.uuid4()), "title": "Mobility Solutions", "description": "Integrated services supporting all operational movement needs.", "image_url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=800"}
    ]

    # Insert into 'content' collection
    # page="business", subpage="hospitality", section="at-a-glance"
    # page="business", subpage="hospitality", section="our-business"

    print("Migrating Travel data to MongoDB...")
    
    # At a Glance
    await db.content.update_one(
        {"page": "business", "subpage": "hospitality", "section": "at-a-glance"},
        {"$set": {
            "page": "business",
            "subpage": "hospitality",
            "section": "at-a-glance",
            "type": "cards",
            "content": at_a_glance_cards,
            "status": "published",
            "updated_at": datetime.utcnow()
        }},
        upsert=True
    )

    # Our Businesses
    await db.content.update_one(
        {"page": "business", "subpage": "hospitality", "section": "our-business"},
        {"$set": {
            "page": "business",
            "subpage": "hospitality",
            "section": "our-business",
            "type": "cards",
            "content": our_travel_businesses,
            "status": "published",
            "updated_at": datetime.utcnow()
        }},
        upsert=True
    )

    print("Travel data migration completed!")
    client.close()

if __name__ == "__main__":
    asyncio.run(migrate_travel_data())
