from pydantic import BaseModel


class RatingCreate(BaseModel):
    movie_id: int
    rating: float
    comment: str


class RatingUpdate(BaseModel):
    rating: float = None
    comment: str = None


class RatingInDBBase(RatingCreate):
    id: int

    class Config:
        orm_mode = True


class Rating(RatingInDBBase):
    pass
