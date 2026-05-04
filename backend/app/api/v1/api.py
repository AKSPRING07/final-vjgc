from app.api.v1.endpoints import about, media

api_router = APIRouter()
api_router.include_router(about.router, prefix="/about", tags=["about"])
api_router.include_router(media.router, prefix="/media", tags=["media"])
# Add more routers here as they are created:
# api_router.include_router(services.router, prefix="/services", tags=["services"])
# api_router.include_router(blog.router, prefix="/blog", tags=["blog"])
