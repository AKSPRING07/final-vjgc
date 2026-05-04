from sqlalchemy import Column, Integer, String, Text, Boolean
from app.db.base_class import Base

class Service(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    icon = Column(String(100), nullable=True) # Icon class or image name
    summary = Column(String(500), nullable=True)
    content = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
