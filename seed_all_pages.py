"""
Seeds all admin-editable pages into universal_content.
Run once from: c:\Users\ELCOT\vjs-website-\backend
  python seed_all_pages.py
"""
from pymongo import MongoClient, UpdateOne
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["vjs_cms"]
col = db["universal_content"]

NOW = datetime.utcnow()

SEED_DATA = [

    # ─────────────────── HOME ──────────────────────────────────────────────
    {"mainPage": "Home", "subSection": "", "category": "Hero Section", "order": 0,
     "title": "Vijayalakshmi Group of Companies",
     "description": "A legacy built on trust, innovation, and excellence across 10 business verticals.",
     "image": "/static/images/assets/hero-bg.jpg"},

    {"mainPage": "Home", "subSection": "", "category": "Services", "order": 0,
     "title": "IT Consulting",
     "description": "Cutting-edge infrastructure and cloud solutions for modern enterprises.",
     "image": "/static/images/assets/it.jpg"},
    {"mainPage": "Home", "subSection": "", "category": "Services", "order": 1,
     "title": "Green Energy",
     "description": "Sustainable solar manufacturing and green energy solutions.",
     "image": "/static/images/assets/solar.jpg"},
    {"mainPage": "Home", "subSection": "", "category": "Services", "order": 2,
     "title": "Logistics",
     "description": "End-to-end logistics and supply chain management.",
     "image": "/static/images/assets/logistics.jpg"},

    {"mainPage": "Home", "subSection": "", "category": "Insights / News", "order": 0,
     "title": "VJS Group Expands Solar Manufacturing Capacity",
     "description": "New plant to produce 500 MW of solar panels annually.",
     "image": "/static/images/assets/news1.jpg"},
    {"mainPage": "Home", "subSection": "", "category": "Insights / News", "order": 1,
     "title": "IT Training Centre Inaugurated",
     "description": "World-class facility opened in Chennai to train 5000+ students.",
     "image": "/static/images/assets/news2.jpg"},

    # ─────────────────── ABOUT - ABOUT GROUP ────────────────────────────────
    {"mainPage": "About", "subSection": "About Group", "category": "Hero Section", "order": 0,
     "title": "About Vijayalakshmi Group",
     "description": "A diversified conglomerate with a presence across 10 industries.",
     "image": "/static/images/assets/about-hero.jpg"},

    {"mainPage": "About", "subSection": "About Group", "category": "News Section", "order": 0,
     "title": "Group Celebrates 30 Years of Excellence",
     "description": "Three decades of growth, sustainability, and community impact.",
     "image": "/static/images/assets/news3.jpg"},

    # ─────────────────── ABOUT - LEADERSHIP ────────────────────────────────
    {"mainPage": "About", "subSection": "Leadership", "category": "Advisors", "order": 0,
     "title": "Mr. Vijayakumar R",
     "description": "Chairman & Managing Director — Visionary leader with 30+ years of experience.",
     "image": "/static/images/assets/advisor1.jpg"},
    {"mainPage": "About", "subSection": "Leadership", "category": "Advisors", "order": 1,
     "title": "Mrs. Lakshmi V",
     "description": "Executive Director — Drives strategic partnerships and global expansion.",
     "image": "/static/images/assets/advisor2.jpg"},
    {"mainPage": "About", "subSection": "Leadership", "category": "Advisors", "order": 2,
     "title": "Mr. Arun Kumar",
     "description": "Chief Financial Officer — Oversees financial planning and risk management.",
     "image": "/static/images/assets/advisor3.jpg"},

    # ─────────────────── ABOUT - AWARDS ────────────────────────────────────
    {"mainPage": "About", "subSection": "Awards", "category": "Awards", "order": 0,
     "title": "Best Employer Award 2023",
     "description": "Recognised by the National HR Council for outstanding employee welfare.",
     "image": "/static/images/assets/award1.jpg"},
    {"mainPage": "About", "subSection": "Awards", "category": "Awards", "order": 1,
     "title": "Green Energy Innovator 2022",
     "description": "Awarded by the Ministry of New & Renewable Energy.",
     "image": "/static/images/assets/award2.jpg"},
    {"mainPage": "About", "subSection": "Awards", "category": "Awards", "order": 2,
     "title": "Export Excellence Trophy 2021",
     "description": "Federation of Indian Export Organisations — Gold Category.",
     "image": "/static/images/assets/award3.jpg"},

    # ─────────────────── NEWSROOM - MEDIA RELEASE ──────────────────────────
    {"mainPage": "Newsroom", "subSection": "Media Release", "category": "News", "order": 0,
     "title": "VJS Group Partners with IIT Madras for AI Research",
     "description": "A landmark MOU signed to drive AI-powered solutions in logistics.",
     "image": "/static/images/assets/press1.jpg"},
    {"mainPage": "Newsroom", "subSection": "Media Release", "category": "News", "order": 1,
     "title": "New Export Hub Launched in Chennai Port",
     "description": "State-of-the-art facility to handle 2000 containers per month.",
     "image": "/static/images/assets/press2.jpg"},
    {"mainPage": "Newsroom", "subSection": "Media Release", "category": "News", "order": 2,
     "title": "Yoga & Wellness Division Opens 10th Centre",
     "description": "Expanding holistic healthcare across Tamil Nadu.",
     "image": "/static/images/assets/press3.jpg"},

    # ─────────────────── BLOG ───────────────────────────────────────────────
    {"mainPage": "Blog", "subSection": "", "category": "News", "order": 0,
     "title": "Top 5 Trends in IT Infrastructure for 2025",
     "description": "Explore how cloud-native architecture is reshaping enterprise IT.",
     "image": "/static/images/assets/blog1.jpg"},
    {"mainPage": "Blog", "subSection": "", "category": "News", "order": 1,
     "title": "Sustainable Plantations: A Growing Investment",
     "description": "Why exotic tree farming is the next big asset class in India.",
     "image": "/static/images/assets/blog2.jpg"},
    {"mainPage": "Blog", "subSection": "", "category": "News", "order": 2,
     "title": "The Future of Solar in South India",
     "description": "Government incentives and market dynamics driving solar adoption.",
     "image": "/static/images/assets/blog3.jpg"},
]

ops = []
for item in SEED_DATA:
    item["isActive"] = True
    item["updatedAt"] = NOW
    filter_key = {
        "mainPage":   item["mainPage"],
        "subSection": item["subSection"],
        "category":   item["category"],
        "title":      item["title"],
    }
    ops.append(UpdateOne(
        filter_key,
        {"$set": item, "$setOnInsert": {"createdAt": NOW}},
        upsert=True
    ))

result = col.bulk_write(ops)
print(f"Done! Matched={result.matched_count}  Upserted={result.upserted_count}  Modified={result.modified_count}")
client.close()
