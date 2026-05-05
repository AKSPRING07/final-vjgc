import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

async def seed_database():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    
    # --- Seed News ---
    news_items = [
        {
            "title": "Connecting India: Unlocking Opportunities Through Connectivity",
            "author": "Rashed Ka",
            "content": "Connecting India: Unlocking Opportunities Through Connectivity",
            "image_url": "/static/images/news video/transport-victoria-2025-12-17-05-37-19-utc.mp4",
            "created_at": datetime(2023, 7, 18)
        },
        {
            "title": "Coding in the Modern Era: Powering Technology and Transformation",
            "author": "Mark Joe",
            "content": "Coding in the Modern Era: Powering Technology and Transformation",
            "image_url": "/static/images/news video/Code.mp4",
            "created_at": datetime(2023, 2, 9)
        },
        {
            "title": "Sustainable Agriculture: Integrating Technology with Tradition",
            "author": "AgriTech Team",
            "content": "Sustainable Agriculture: Integrating Technology with Tradition",
            "image_url": "/static/images/hero video/farm-agricultural-field-leveling-tractor-farm-work-2026-01-22-22-50-45-utc.mp4",
            "created_at": datetime(2023, 10, 12)
        },
        {
            "title": "Scientific Breakthroughs in Eco-Friendly Industrial Solutions",
            "author": "R&D Hub",
            "content": "Scientific Breakthroughs in Eco-Friendly Industrial Solutions",
            "image_url": "/static/images/hero video/scientist-pours-chemicals-from-a-test-tube-into-a-2025-12-17-07-28-37-utc.mp4",
            "created_at": datetime(2023, 11, 25)
        }
    ]
    
    # --- Seed Services ---
    services = [
        {
            "title": "IT Consulting & Services",
            "description": "Providing innovative digital solutions and enterprise IT infrastructure.",
            "icon_url": "/static/images/icon/icon_17_dual.svg"
        },
        {
            "title": "Education & Training",
            "description": "Offering quality education and skill development programs to empower students.",
            "icon_url": "/static/images/icon/icon_18_dual.svg"
        },
        {
            "title": "Green Energy Solutions",
            "description": "Sustainable solar manufacturing and eco-friendly power alternatives.",
            "icon_url": "/static/images/icon/icon_19_dual.svg"
        },
        {
            "title": "Business Consulting",
            "description": "Helping businesses grow with strategic planning, expert guidance, and actionable solutions.",
            "icon_url": "/static/images/icon/icon_20_dual.svg"
        }
    ]

    # Insert News
    print("Clearing old news and inserting default news...")
    await db.news.delete_many({})
    await db.news.insert_many(news_items)
    
    # Insert Services
    print("Clearing old services and inserting default services...")
    await db.services.delete_many({})
    await db.services.insert_many(services)
    
    print("Database seeding completed successfully! You can now check the Admin panel and website.")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())
