from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models.about import About as AboutModel
from app.schemas.about import About, AboutCreate, AboutUpdate

router = APIRouter()

@router.get("/", response_model=About)
def read_about(db: Session = Depends(deps.get_db)) -> Any:
    """
    Get About Us content.
    """
    about = db.query(AboutModel).first()
    if not about:
        raise HTTPException(status_code=404, detail="About content not found")
    return about

@router.put("/", response_model=About)
def update_about(
    *,
    db: Session = Depends(deps.get_db),
    about_in: AboutUpdate
) -> Any:
    """
    Update About Us content.
    """
    about = db.query(AboutModel).first()
    if not about:
        # Create it if it doesn't exist
        about = AboutModel(**about_in.dict())
        db.add(about)
    else:
        update_data = about_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(about, field, update_data[field])
    db.commit()
    db.refresh(about)
    return about
