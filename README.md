## API de Filmes e Avaliações

  <li> Este projeto é uma API REST que permite gerenciar filmes e avaliações de filmes. 
  <li> A API foi desenvolvida usando o framework FastAPI em Python e armazena dados em um arquivo JSON (primeira parte).
  <li> Para a entrega final espera-se a integração da FastAPi há um banco de dados (mysql o nosso) por meio do ORM SQLalchemy.

## Funcionalidades

### Filmes
 <li> GET /movies: Retorna uma lista com todos os filmes cadastrados.
 <li>GET /movies/{movie_id}: Retorna informações sobre um filme específico.
 <li>POST /movies: Cadastra um novo filme.
 <li>PUT /movies/{movie_id}: Atualiza informações de um filme existente.
 <li>DELETE /movies/{movie_id}: Remove um filme do sistema, junto com todas as avaliações associadas a ele.

### Avaliações
  <li> GET /ratings/{movie_id}: Retorna todas as avaliações de um filme específico.
  <li> POST /ratings: Cadastra uma nova avaliação.


## Campos

### Os campos disponíveis para filmes e avaliações são:

### Filmes

  <li>id: Identificador único do filme (inteiro).
  <li>title: Título do filme (texto).
  <li>Genre:Gênero do filme(texto)
  <li> director : diretor do filme(texto)
  <li>year: ano lançamento(inteiro)
  <li> synopsis:sinopse do filme(texto)

### Avaliações

  <li> id: Identificador único da avaliação (inteiro).
  <li> movie_id: Identificador do filme associado à avaliação (inteiro).
  <li> rating: Avaliação do filme, de 0 a 10 (decimal).
  <li> comment: Comentário sobre o filme (texto).

## Atualizações

### Avaliações
<li> GET /ratings/: Retorna todas as avaliações de todos os filmes (lista de filmes).
<li> POST /ratings: Cadastra uma nova avaliação somente se houver uma ou mais avaliações relacionados a esse filme .
<li> (opcional) PUT /ratings: Atualizar a avaliação de um filme existente.
<li> (opcional) DELETE /ratings: Deleta a avaliação específica de um filme existente.

### Database
<li> Criação de um banco de dados no mysql e integração do banco de dados por SQLalchemy com as rotas feitas para cada função (get, post, put e delete).
<li> No docs do fastapi o CRUD alterará o banco de dados para movies e ratings.

### Arquivo main
<li> O arquivo main.py agora não conterá as funções de criação do CRUD, mas conterá as rotas das classes movies e ratings e a criação das tabelas no banco de dados

### Acesso as credenciais
<li> criação de credenciais (não estarão no repositório remoto) em um arquivo .env para a integração do banco de dados e a API

## Utilização  da API
A API estará disponível pelo FastAPI -Swagger UI em:
http://localhost:8000/docs# a ser executada com o código pelo terminal de comando da sua máquina:
```
uvicorn main:app --reload
```

## Links Youtube

### Primeira Parte
<li> Link Explicação Youtube: https://youtu.be/oVQcdEAvk_w

### Entrega Final
<li> Link PF: link aqui
