from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api import public, admin, auth, content, cms
from pathlib import Path
import os

app = FastAPI(title=settings.PROJECT_NAME)


# Setup Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Serve static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Setup Templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# --- Compatibility Bridge for Flask Templates ---
from jinja2 import pass_context

@pass_context
def safe_url_for(context: dict, name: str, **params):
    request = context["request"]
    try:
        if name == "static" and "filename" in params:
            params["path"] = params.pop("filename")
        return str(request.url_for(name, **params))
    except Exception:
        return "#"

templates.env.globals["url_for"] = safe_url_for

# Global Error Handler
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    import traceback
    return PlainTextResponse(f"DEBUG ERROR: {str(exc)}\n\n{traceback.format_exc()}", status_code=500)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static Files
if not os.path.exists("uploads"):
    os.makedirs("uploads")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="../static"), name="static")
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Include Routers
app.include_router(public.router, prefix="/api", tags=["Public"])
app.include_router(auth.router, prefix="/api/admin", tags=["Auth"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(cms.router, prefix="/api/admin/cms", tags=["CMS"])
app.include_router(content.router, prefix="/api/content", tags=["Content Management"])

from app.db.mongodb import get_database

async def get_page_context(path: str):
    db = get_database()
    context = {}
    
    if path == "index-2" or path == "":
        # Fetch latest services and news for home page
        services = []
        async for doc in db["services"].find().limit(6):
            doc["_id"] = str(doc["_id"])
            services.append(doc)
        context["services"] = services
        
        news = []
        async for doc in db["news"].find().sort("created_at", -1).limit(4):
            doc["_id"] = str(doc["_id"])
            news.append(doc)
        context["news"] = news
        
    elif "about" in path:
        about = await db["about"].find_one()
        if about:
            about["_id"] = str(about["_id"])
            context["about"] = about
            
    elif "service" in path:
        services = []
        async for doc in db["services"].find():
            doc["_id"] = str(doc["_id"])
            services.append(doc)
        context["services"] = services
        
    elif "news" in path or "blog" in path:
        news = []
        async for doc in db["news"].find().sort("created_at", -1):
            doc["_id"] = str(doc["_id"])
            news.append(doc)
        context["news"] = news
        
    # Fetch all published CMS content for this page/subpage
    # Mapping specific template paths to our CMS Page/Subpage structure
    path_map = {
        "index-2": ("home", None),
        "": ("home", None),
        "about-us-v2": ("about", "about-group"),
        "about-us-v1": ("about", "journey"),
        "service-v1": ("about", "leadership"),
        "media-release": ("newsroom", "media-release"),
        "data-centers-hosting": ("business", "data-centers"),
        "it-consulting": ("business", "it-consulting"),
        "green-energy": ("business", "green-energy"),
        "logistics-services": ("business", "logistics"),
        "export-import": ("business", "export-import"),
        "property-services": ("business", "property-services"),
        "it-training": ("business", "it-training"),
        "yoga-wellness": ("business", "yoga-wellness"),
        "travel-rentals": ("business", "travel-rentals"),
        "plantations": ("business", "plantations")
    }
    
    page_key, subpage_key = path_map.get(path, (path.split('-')[0], None))
    
    query = {"page": page_key, "status": "published"}
    if subpage_key:
        query["subpage"] = subpage_key
    else:
        query["$or"] = [{"subpage": None}, {"subpage": {"$exists": False}}, {"subpage": ""}]

    # Initialize cms_content with empty defaults to prevent Jinja2 'Undefined' errors
    cms_content = {
        "hero": {"content": {}},
        "cards": {"content": []},
        "text": {"content": {}},
        "news": {"content": []}
    }
    
    async for doc in db["content"].find(query):
        cms_content[doc["section"]] = doc
    context["cms"] = cms_content
    
    return context

# Serve Website Pages
@app.get("/{path}", name="dynamic_route")
async def dynamic_route(request: Request, path: str):
    try:
        clean_path = path.replace(".html", "")
        template_file = f"{clean_path}.html"
        context = await get_page_context(clean_path)
        return templates.TemplateResponse(request, template_file, context)
    except Exception as e:
        # Fallback to home if page not found
        return templates.TemplateResponse(request, "index-2.html", await get_page_context("index-2"))

@app.get("/", name="home")
async def home(request: Request):
    context = await get_page_context("index-2")
    return templates.TemplateResponse(request, "index-2.html", context)

