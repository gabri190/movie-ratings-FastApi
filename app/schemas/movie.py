from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    genre: str
    director: str
    year: int
    synopsis: str


class MovieUpdate(BaseModel):
    title: str = None
    genre: str = None
    director: str = None
    year: int = None
    synopsis: str = None


class MovieInDBBase(MovieCreate):
    id: int

    class Config:
        orm_mode = True


class Movie(MovieInDBBase):
    pass
