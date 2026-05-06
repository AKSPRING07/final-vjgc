
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def migrate_7_videos():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Migrating 7 hero videos to Home page CMS...")
    
    # First, clear existing hero items for Home to avoid duplicates if we want exactly 7
    # Or we can just insert them if they don't exist.
    
    videos = [
        {
            "title": "Building Stronger Communities Together",
            "video": "/static/images/hero video/african-american-mother-playing-with-her-daughters-2026-01-20-18-10-31-utc.mp4",
            "cta": "Our Values"
        },
        {
            "title": "Innovative Agricultural Solutions",
            "video": "/static/images/hero video/farm-agricultural-field-leveling-tractor-farm-work-2026-01-22-22-50-45-utc.mp4",
            "cta": "Learn More"
        },
        {
            "title": "Global Logistics and Supply Chain",
            "video": "/static/images/hero video/freight-transport-2025-12-17-20-47-07-utc.mp4",
            "cta": "Explore Services"
        },
        {
            "title": "Enterprise Business Consulting",
            "video": "/static/images/hero video/people-meeting-and-documents-in-office-for-busine-2026-01-22-06-04-12-utc.mp4",
            "cta": "Work With Us"
        },
        {
            "title": "Empowering Education & Skill Building",
            "video": "/static/images/hero video/professor-classroom-and-student-with-question-for-2025-12-17-23-05-05-utc.mp4",
            "cta": "Our Programs"
        },
        {
            "title": "Eco-Friendly Industrial Breakthroughs",
            "video": "/static/images/hero video/scientist-pours-chemicals-from-a-test-tube-into-a-2025-12-17-07-28-37-utc.mp4",
            "cta": "Read More"
        },
        {
            "title": "Holistic Yoga & Wellness Programs",
            "video": "/static/images/hero video/yoga-2026-01-21-05-24-27-utc.mp4",
            "cta": "Join Us"
        }
    ]

    # Delete existing hero items for Home to ensure exact 7 sequence
    await db["universal_content"].delete_many({
        "mainPage": "Home",
        "category": "Hero Section"
    })

    for i, item in enumerate(videos):
        new_doc = {
            "mainPage": "Home",
            "subSection": "",
            "category": "Hero Section",
            "title": item["title"],
            "image": item["video"], # Using image field for URL
            "cta_text": item["cta"],
            "isActive": True,
            "order": i,
            "updatedAt": datetime.now()
        }
        await db["universal_content"].insert_one(new_doc)
        print(f"Added Hero Slide {i+1}: {item['title']}")

if __name__ == "__main__":
    asyncio.run(migrate_7_videos())
