## API de Filmes e Avaliações

- Este projeto é uma API REST que permite gerenciar filmes e avaliações de filmes. 
- A API foi desenvolvida usando o framework FastAPI em Python e armazena dados em um arquivo JSON (primeira parte).
- Para a entrega final espera-se a integração da FastAPi há um banco de dados (mysql o nosso) por meio do ORM SQLalchemy.

## Funcionalidades

### Filmes
- GET /movies: Retorna uma lista com todos os filmes cadastrados.
- GET /movies/{movie_id}: Retorna informações sobre um filme específico.
- POST /movies: Cadastra um novo filme.
- PUT /movies/{movie_id}: Atualiza informações de um filme existente.
- DELETE /movies/{movie_id}: Remove um filme do sistema, junto com todas as avaliações associadas a ele.

### Avaliações
- GET /ratings/{movie_id}: Retorna todas as avaliações de um filme específico.
- POST /ratings: Cadastra uma nova avaliação.

## Campos

### Os campos disponíveis para filmes e avaliações são:

### Filmes

- id: Identificador único do filme (inteiro).
- title: Título do filme (texto).
- Genre:Gênero do filme(texto)
- director : diretor do filme(texto)
- year: ano lançamento(inteiro)
- synopsis:sinopse do filme(texto)

### Avaliações

- id: Identificador único da avaliação (inteiro).
- movie_id: Identificador do filme associado à avaliação (inteiro).
- rating: Avaliação do filme, de 0 a 10 (decimal).
- comment: Comentário sobre o filme (texto).

## Atualizações

### Avaliações

- GET /ratings/: Retorna todas as avaliações de todos os filmes (lista de filmes).
- POST /ratings: Cadastra uma nova avaliação somente se houver uma ou mais avaliações relacionados a esse filme .
- (opcional) PUT /ratings: Atualizar a avaliação de um filme existente.
- (opcional) DELETE /ratings: Deleta a avaliação específica de um filme existente.

### Database

- Criação de um banco de dados no mysql e integração do banco de dados por SQLalchemy com as rotas feitas para cada função (get, post, put e delete).
- No docs do fastapi o CRUD alterará o banco de dados para movies e ratings.

### Arquivo main

- O arquivo main.py agora não conterá as funções de criação do CRUD, mas conterá as rotas das classes movies e ratings e a criação das tabelas no banco de dados

### Acesso as credenciais

- Criação de credenciais (não estarão no repositório remoto) em um arquivo .env para a integração do banco de dados e a API

## Utilização  da API

- Antes de utilizar a API adicione um arquivo .env como no exemplo abaixo:

```
DB_PROVIDER=mysql
DB_DRIVER=mysqlconnector
DB_DATABASE_NAME=Movies
DB_USER="my-user"
DB_PASSWORD="MyPassword"
DB_HOST=localhost
DB_PORT=3306
  
DB_CONNECTION_STRING=${DB_PROVIDER}+${DB_DRIVER}://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE_NAME}

```
Nele, você pode trocar o usuário e senha pelo banco de dados correspondente que vc criou!
  
  
A API estará disponível pelo FastAPI -Swagger UI em:
http://localhost:8000/docs# a ser executada com o código pelo terminal de comando da sua máquina:
```
uvicorn main:app --reload
```

## Links Youtube

### Primeira Parte
- Link Explicação Youtube: https://youtu.be/oVQcdEAvk_w

### Entrega Final
- Link PF: https://www.youtube.com/watch?v=sI1YNcSPE1E&feature=youtu.be
