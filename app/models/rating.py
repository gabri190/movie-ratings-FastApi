from sqlalchemy import Column, Integer, Float, String, ForeignKey,CheckConstraint
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    movie = relationship("Movie", back_populates="ratings")
    rating = Column(Float, CheckConstraint('rating >= 0 AND rating <= 10'))
    comment = Column(String(100), nullable=True)

 