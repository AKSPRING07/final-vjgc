from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "VJS CMS Backend"
    
    # MongoDB Atlas Config
    MONGO_URI: str = "mongodb+srv://user:pass@cluster.mongodb.net/vjs_cms?retryWrites=true&w=majority"
    DATABASE_NAME: str = "vjs_cms"
    PORT: int = 8000 # Default to 8000, but .env will override to 5000
    
    # Security
    SECRET_KEY: str = "super-secret-key-for-jwt" # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 Days
    
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        case_sensitive = False
        env_file = ".env"
        extra = "ignore" # Allow extra fields in .env without crashing

settings = Settings()
