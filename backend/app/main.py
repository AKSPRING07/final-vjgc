from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api import public, admin, auth
import os

app = FastAPI(title=settings.PROJECT_NAME)

# Ensure uploads directory exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Serve static files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Events
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Include Routers
app.include_router(public.router, prefix="/api", tags=["Public"])
app.include_router(auth.router, prefix="/api/admin", tags=["Auth"]) # login is /api/admin/login
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

from app.db.mongodb import get_database
from fastapi import Depends

@app.get("/api/debug/achievements")
async def debug_achievements(db = Depends(get_database)):
    achievements = []
    cursor = db["achievements"].find().limit(10)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        achievements.append(doc)
    return achievements

@app.get("/")
async def root():
    return {"message": "Welcome to VJS CMS API (MongoDB Atlas)", "docs": "/docs"}
