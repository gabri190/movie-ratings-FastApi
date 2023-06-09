-- SQL EXAMPLE, NOT USED IN THIS PROJECT

DROP DATABASE IF EXISTS Movies;
CREATE DATABASE Movies;

USE Movies;

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    director VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    synopsis VARCHAR(500) NOT NULL
);


DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id),
    rating FLOAT(3,2) NOT NULL CHECK (rating >= 0 AND rating <= 10)
    comment VARCHAR(500)
);
