from sqlalchemy import Column, Integer, String, Text, Date
from app.db.base_class import Base

class Achievement(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    date = Column(Date, nullable=True)
    image_url = Column(String(500), nullable=True)
