from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["vjs_cms"]
col = db["universal_content"]

news_items = [
    {
        "mainPage": "Newsroom",
        "subSection": "Media Release",
        "category": "News",
        "title": "VJS Group Partners with IIT Madras for AI Research",
        "description": "A landmark MOU signed to drive AI-powered solutions in logistics.",
        "image": "/static/images/assets/press1.jpg",
        "isActive": True,
        "updatedAt": datetime.utcnow(),
        "order": 0
    },
    {
        "mainPage": "Newsroom",
        "subSection": "Media Release",
        "category": "News",
        "title": "New Export Hub Launched in Chennai Port",
        "description": "State-of-the-art facility to handle 2000 containers per month.",
        "image": "/static/images/assets/press2.jpg",
        "isActive": True,
        "updatedAt": datetime.utcnow(),
        "order": 1
    }
]

for item in news_items:
    col.update_one(
        {"mainPage": item["mainPage"], "subSection": item["subSection"], "category": item["category"], "title": item["title"]},
        {"$set": item, "$setOnInsert": {"createdAt": datetime.utcnow()}},
        upsert=True
    )

print("News items seeded successfully")
client.close()
