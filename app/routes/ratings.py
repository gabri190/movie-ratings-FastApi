from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func


from app.schemas.rating import Rating as Rating_Schemas,RatingCreate,RatingUpdate
from app.database.connection import get_db
from app.models.rating  import Rating as RatingModel
from app.models.movie import Movie as MovieModel
from typing import List

router = APIRouter()

#retorn uma lista de avaliacoes
@router.get("/ratings", response_model=List[Rating_Schemas])
def get_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ratings = db.query(RatingModel).offset(skip).limit(limit).all()
    return ratings
#retorna uma avaliacao pelo movie_id
@router.get("/ratings/{movie_id}")
def get_movie_ratings(movie_id: int, db: Session = Depends(get_db)):
    rating = db.query(RatingModel).filter(RatingModel.id == movie_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Movie not found")
    return rating
#cria uma nova avaliação se ja tiver filme correspondente
@router.post("/ratings", response_model=Rating_Schemas)
def create_ratings(rating: RatingCreate, db: Session = Depends(get_db)):
    # Check if the specified movie_id exists
    movie = db.query(MovieModel).filter(MovieModel.id == rating.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_rating = RatingModel(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

#altera uma avaliação se ja tiver filme correspondente
@router.put("/ratings/{movie_id}", response_model=Rating_Schemas)
def update_ratings(movie_id: int, movie: RatingUpdate, db: Session = Depends(get_db)):
    db_rating = db.query(RatingModel).filter(RatingModel.movie_id == movie_id).first()
    if not db_rating:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.dict().items():
        setattr(db_rating, key, value)
    db.commit()
    db.refresh(db_rating)
    return db_rating

#deleta uma avaliação de determinado id
@router.delete("/ratings/{movie_id}")
def delete_ratings(movie_id: int, db: Session = Depends(get_db)):
    db_rating = db.query(RatingModel).filter(RatingModel.id == movie_id).first()
    if not db_rating:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_rating)
    db.commit()
    return {"detail": "Movie deleted"}
