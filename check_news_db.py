from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["vjs_cms"]
col = db["universal_content"]

print("--- ALL DOCUMENTS IN universal_content ---")
for doc in col.find():
    print(f"Page: {doc.get('mainPage')}, Sub: {doc.get('subSection')}, Cat: {doc.get('category')}, Title: {doc.get('title')}")

client.close()
