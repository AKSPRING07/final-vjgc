from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.core.config import settings

router = APIRouter()

# Simple hardcoded admin for demonstration
# In production, you would fetch this from MongoDB
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = security.get_password_hash("vjs_admin_123") 

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login endpoint to get JWT access token.
    Accepts 'username' and 'password' as form-data.
    """
    if form_data.username != ADMIN_USERNAME or not security.verify_password(form_data.password, ADMIN_PASSWORD_HASH):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(subject=form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}
