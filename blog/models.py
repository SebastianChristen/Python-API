from sqlalchemy import Column, Integer, String
from .database import Base

# Convert a Table to an Object and vice-versa
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key = True)
    title = Column(String)

