from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func

from app.schemas.movie import Movie as Movie_Schemas,MovieCreate,MovieUpdate
from app.database.connection import get_db
from app.models.movie import Movie as MovieModel
from app.models.rating import Rating as RatingModel

router = APIRouter()

#retorna lista de filmes
@router.get("/movies", response_model=List[Movie_Schemas])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = db.query(MovieModel).offset(skip).limit(limit).all()
    return movies

#retorna o filme pelo respectivo id
@router.get("/movies/{movie_id}", response_model=Movie_Schemas)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

#cria um novo filme
@router.post("/movies", response_model=Movie_Schemas)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = MovieModel(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
#altera dados do filme
@router.put("/movies/{movie_id}", response_model=Movie_Schemas)
def update_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.dict().items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

#deleta um filme e todas as avaliações realacionadas a ele
@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.query(RatingModel).filter(RatingModel.movie_id == movie_id).delete()

    db.commit()
    return {"detail": "Movie deleted"}

