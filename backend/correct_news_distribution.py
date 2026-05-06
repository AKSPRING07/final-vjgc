
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def migrate_and_correct():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Correcting news distribution...")
    
    # 1. Move the 4 legacy news items to HOME page
    async for doc in db["news"].find():
        # Check if already in Home -> Insights / News
        exists = await db["universal_content"].find_one({
            "mainPage": "Home",
            "category": "Insights / News",
            "title": doc["title"]
        })
        
        if not exists:
            new_doc = {
                "mainPage": "Home",
                "subSection": "",
                "category": "Insights / News",
                "title": doc.get("title", ""),
                "description": doc.get("content", ""),
                "image": doc.get("image_url", ""),
                "author": doc.get("author", "Admin"),
                "isActive": True,
                "order": 0,
                "updatedAt": datetime.now()
            }
            await db["universal_content"].insert_one(new_doc)
            print(f"Moved to Home: {doc['title']}")
        else:
            print(f"Already in Home: {doc['title']}")

    # 2. Delete the incorrectly placed news from About page
    # But only those that were legacy news items
    legacy_titles = [
        "Connecting India: Unlocking Opportunities Through Connectivity",
        "Coding in the Modern Era: Powering Technology and Transformation",
        "Sustainable Agriculture: Integrating Technology with Tradition",
        "Scientific Breakthroughs in Eco-Friendly Industrial Solutions"
    ]
    await db["universal_content"].delete_many({
        "mainPage": "About",
        "category": "Insights News",
        "title": {"$in": legacy_titles}
    })
    print("Removed incorrectly placed news from About page.")

    # 3. Create specific news for About page (Insights News)
    about_news = [
        {
            "title": "Aditya Institute: Empowering Education through Innovation.",
            "description": "Offering quality education and skill development programs to empower students.",
            "image": "/static/images/image/news/aditya institute1.jpg",
            "author": "Education Team"
        },
        {
            "title": "Agham Grham: Sustainable Housing Solutions.",
            "description": "Building sustainable and affordable housing for a better tomorrow.",
            "image": "/static/images/image/news/agham grham 1.jpg",
            "author": "Real Estate"
        },
        {
            "title": "Springreen: Leading the Green Revolution.",
            "description": "Innovative solutions for a sustainable and eco-friendly future.",
            "image": "/static/images/image/news/springreen1.jpg",
            "author": "Energy Team"
        },
        {
            "title": "Springreen Break: Eco-friendly Industrial Milestones.",
            "description": "Reaching new heights in sustainable industrial development.",
            "image": "/static/images/image/news/springreen break.jpg",
            "author": "Industry Hub"
        }
    ]

    for item in about_news:
        exists = await db["universal_content"].find_one({
            "mainPage": "About",
            "category": "Insights News",
            "title": item["title"]
        })
        if not exists:
            item.update({
                "mainPage": "About",
                "subSection": "About Group",
                "category": "Insights News",
                "isActive": True,
                "order": 0,
                "updatedAt": datetime.now()
            })
            await db["universal_content"].insert_one(item)
            print(f"Added to About: {item['title']}")

if __name__ == "__main__":
    asyncio.run(migrate_and_correct())
