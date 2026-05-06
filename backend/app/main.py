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
        pass
        
    elif "about" in path:
        pass
            
    elif "service" in path:
        pass
        
    elif "news" in path or "blog" in path:
        pass
        
    # Fetch all published CMS content for this page/subpage
    # Map specific template paths to our CMS Main Page / Sub-Section structure
    path_map = {
        "": ("Home", ""),
        "index-2": ("Home", ""),
        "about-us-v2": ("About", "About Group"),
        "about-us-v1": ("About", "Our Journey"),
        "service-v1": ("About", "Leadership"),
        "media-release": ("Newsroom", "Media Release"),
        "media-kit": ("Newsroom", "Media Kit"),
        "blog-v1": ("Foundation", ""),
        # Business Verticals
        "data-centers-hosting": ("Business Verticals", "Enterprise Data Centers & Hosting Services"),
        "it-consulting": ("Business Verticals", "IT Consulting"),
        "green-energy": ("Business Verticals", "Green Energy & Solar Manufacturing"),
        "logistics-services": ("Business Verticals", "Logistics Services"),
        "export-import": ("Business Verticals", "Export & Import"),
        "property-services": ("Business Verticals", "Property Services"),
        "it-training": ("Business Verticals", "IT Training"),
        "yoga-wellness": ("Business Verticals", "Yoga & Wellness"),
        "travel-rentals": ("Business Verticals", "Travel & Rentals"),
        "plantations": ("Business Verticals", "Plantations & Exotic Trees"),
        "plantations-exotic-trees": ("Business Verticals", "Plantations & Exotic Trees")
    }
    
    # Normalize path
    clean_path = path
    if clean_path.endswith(".html"):
        clean_path = clean_path[:-5]
    if clean_path == "index":
        clean_path = ""
        
    page_name, sub_name = path_map.get(clean_path, (clean_path, ""))
    
    # Ensure sub_name is a string
    sub_name = sub_name or ""
    
    query = {"mainPage": {"$regex": f"^{page_name}$", "$options": "i"}, "isActive": True}
    if sub_name:
        query["subSection"] = sub_name
    else:
        # For pages without a specific subSection, match empty string or None
        query["subSection"] = {"$in": ["", None]}

    
    print(f"DEBUG: path='{path}' clean='{clean_path}' page='{page_name}' sub='{sub_name}'")
    print(f"DEBUG: query={query}")
    
    results = []
    async for doc in db["universal_content"].find(query).sort("order", 1):
        doc["_id"] = str(doc.pop("_id"))
        results.append(doc)
    
    print(f"DEBUG: Found {len(results)} results")
    
    class SafeDict(dict):
        def __getitem__(self, key):
            val = super().get(key, {"content": []})
            return val

    # Group by category
    cms_content = SafeDict()
    for doc in results:
        cat = doc.get("category", "General")
        if cat not in cms_content:
            cms_content[cat] = {"content": []}
        
        # Ensure template-friendly aliases
        img_path = doc.get("image") or ""
        doc["image_url"] = img_path
        doc["video_url"] = doc.get("video_url", img_path) if img_path.lower().endswith(".mp4") else ""
        
        cms_content[cat]["content"].append(doc)
        
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

