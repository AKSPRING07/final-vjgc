from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

class About(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    mission = Column(Text, nullable=True)
    vision = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
