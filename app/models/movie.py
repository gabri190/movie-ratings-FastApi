from sqlalchemy import Column, Integer, String
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    genre = Column(String(50), nullable=False)
    director = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    synopsis = Column(String(100), nullable=False)
    ratings = relationship("Rating", back_populates="movie")
