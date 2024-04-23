CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100),
    id_console INTEGER
);

CREATE TABLE IF NOT EXISTS videogames (
    id_console INTEGER,
    name VARCHAR(100),
    id_company INTEGER,
    release_date DATE
);

CREATE TABLE IF NOT EXISTS games (
    id_game SERIAL PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    release_date DATE,
    id_console INTEGER
);

CREATE TABLE IF NOT EXISTS company (
    id_company SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);