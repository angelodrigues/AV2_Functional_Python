CREATE TABLE IF NOT EXISTS games (
    id_game SERIAL PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    release_date DATE,
    id_console INTEGER
);