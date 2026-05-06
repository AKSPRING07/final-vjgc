
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo

SLUG_TO_NAME = {
    "home":     "Home",
    "about":    "About",
    "business": "Business Verticals",
    "newsroom": "Newsroom",
    "blog":     "Blog",
    "about-group":  "About Group",
    "leadership":   "Leadership",
    "awards":       "Awards",
    "journey":      "Our Journey",
    "media-release": "Media Release",
    "it-consulting":      "IT Consulting",
    "data-centers":       "Enterprise Data Centers & Hosting Services",
    "export-import":      "Export & Import",
    "plantations":        "Plantations & Exotic Trees",
    "it-training":        "IT Training",
    "yoga-wellness":      "Yoga & Wellness",
    "property-services":  "Property Services",
    "green-energy":       "Green Energy & Solar Manufacturing",
    "logistics":          "Logistics Services",
    "travel-rentals":     "Travel & Rentals",
    "at-a-glance":    "At a Glance",
    "our-business":   "Our Business",
    "Hero Section":   "Hero Section",
    "Services":       "Services",
    "Insights / News": "Insights / News",
    "Advisors":       "Advisors",
    "Awards":         "Awards",
    "News":           "News",
}

async def fix_names():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Fixing names in universal_content with conflict resolution...")
    async for doc in db["universal_content"].find():
        updates = {}
        
        mainPage = doc.get("mainPage")
        subSection = doc.get("subSection")
        category = doc.get("category")
        title = doc.get("title")
        
        # Determine target values
        target_main = SLUG_TO_NAME.get(mainPage, mainPage)
        target_sub = SLUG_TO_NAME.get(subSection, subSection)
        if subSection == "None": target_sub = ""
        target_cat = SLUG_TO_NAME.get(category, category)
        
        if target_main != mainPage: updates["mainPage"] = target_main
        if target_sub != subSection: updates["subSection"] = target_sub
        if target_cat != category: updates["category"] = target_cat
        
        if updates:
            # Check if updating would cause a duplicate
            new_main = updates.get("mainPage", mainPage)
            new_sub = updates.get("subSection", subSection)
            new_cat = updates.get("category", category)
            
            exists = await db["universal_content"].find_one({
                "mainPage": new_main,
                "subSection": new_sub,
                "category": new_cat,
                "title": title,
                "_id": {"$ne": doc["_id"]}
            })
            
            if exists:
                print(f"Conflict found for {title}. Deleting current doc to favor existing normalized one.")
                await db["universal_content"].delete_one({"_id": doc["_id"]})
            else:
                try:
                    await db["universal_content"].update_one({"_id": doc["_id"]}, {"$set": updates})
                    print(f"Updated {title}: {updates}")
                except pymongo.errors.DuplicateKeyError:
                    print(f"Duplicate error (concurrent) for {title}. Deleting.")
                    await db["universal_content"].delete_one({"_id": doc["_id"]})

if __name__ == "__main__":
    asyncio.run(fix_names())
