from fastapi import FastAPI
from app.routes import movies, ratings
from app.database.connection import Base, engine

app = FastAPI(
    title="Movie Ratings API",
    description="API para gerenciar filmes e avaliações",
    version="1.0.0",
)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Adiciona as rotas para as classes Movie e Rating
app.include_router(movies.router, tags=["Movies"])
app.include_router(ratings.router, tags=["Ratings"])


# Rota principal
@app.get("/", tags=["Main"])
def read_root():
    return {"message": "Welcome to the Movie Ratings API!"}
