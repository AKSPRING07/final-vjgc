import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0")
DATABASE_NAME = "vjs_cms"

async def sync_all_data():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db["universal_content"]

    print(f"Connecting to MongoDB: {DATABASE_NAME}")

    # Define the 10 business verticals
    verticals = [
        "IT Consulting",
        "Enterprise Data Centers & Hosting Services",
        "Export & Import",
        "Plantations & Exotic Trees",
        "IT Training",
        "Yoga & Wellness",
        "Property Services",
        "Green Energy & Solar Manufacturing",
        "Logistics Services",
        "Travel & Rentals"
    ]

    # Initial standard data to seed the database
    seed_data = []

    for vertical in verticals:
        # 1. Add "At a Glance" items
        seed_data.extend([
            {
                "mainPage": "Business Verticals",
                "subSection": vertical,
                "category": "At a Glance",
                "title": f"{vertical} Overview",
                "description": f"Strategic overview of our operations and market leadership in {vertical}.",
                "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1000",
                "order": 1
            },
            {
                "mainPage": "Business Verticals",
                "subSection": vertical,
                "category": "At a Glance",
                "title": "Global Presence",
                "description": f"Our extensive network and global reach in the {vertical} sector.",
                "image": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&q=80&w=1000",
                "order": 2
            },
            {
                "mainPage": "Business Verticals",
                "subSection": vertical,
                "category": "At a Glance",
                "title": "Future Innovation",
                "description": f"Driving the future of {vertical} through sustainable practices and technology.",
                "image": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=1000",
                "order": 3
            }
        ])

        # 2. Add "Our Business" items
        seed_data.extend([
            {
                "mainPage": "Business Verticals",
                "subSection": vertical,
                "category": "Our Business",
                "title": f"VJS {vertical} Solutions",
                "description": f"Comprehensive solutions tailored for the evolving needs of the {vertical} market.",
                "image": "https://images.unsplash.com/photo-1454165833762-02ad50c797e2?auto=format&fit=crop&q=80&w=1000",
                "order": 1
            },
            {
                "mainPage": "Business Verticals",
                "subSection": vertical,
                "category": "Our Business",
                "title": "Strategic Partnerships",
                "description": "Collaborating with industry leaders to deliver exceptional value.",
                "image": "https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&q=80&w=1000",
                "order": 2
            }
        ])

    print(f"Attempting to sync {len(seed_data)} items...")

    count_inserted = 0
    count_updated = 0

    for item in seed_data:
        # UPSERT Logic
        filter_query = {
            "mainPage": item["mainPage"],
            "subSection": item["subSection"],
            "category": item["category"],
            "title": item["title"]
        }
        
        existing = await collection.find_one(filter_query)
        
        if existing:
            # Update
            await collection.update_one(filter_query, {"$set": item})
            count_updated += 1
        else:
            # Insert
            item["createdAt"] = datetime.utcnow()
            item["isActive"] = True
            await collection.insert_one(item)
            count_inserted += 1

    print(f"--- SYNC COMPLETE ---")
    print(f"Inserted: {count_inserted}")
    print(f"Updated: {count_updated}")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(sync_all_data())
