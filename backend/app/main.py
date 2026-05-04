from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api import public, admin, auth
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
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Lifecycle
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

# Serve Website Pages
@app.get("/{path}", name="dynamic_route")
async def dynamic_route(request: Request, path: str):
    try:
        template_file = f"{path}.html" if not path.endswith(".html") else path
        # NEW STYLE: request must be the first argument
        return templates.TemplateResponse(request, template_file, {})
    except Exception as e:
        return PlainTextResponse(f"Page Error: {str(e)}", status_code=404)

@app.get("/", name="home")
async def home(request: Request):
    # NEW STYLE: request must be the first argument
    return templates.TemplateResponse(request, "index-2.html", {})
