INSERT INTO users (name, country, id_console) VALUES
    ('João', 'Brasil', 1),
    ('Maria', 'EUA', 2),
    ('Carlos', 'Espanha', 3);

INSERT INTO videogames (id_console, name, id_company, release_date) VALUES
    (1, 'Super Mario Odyssey', 1, '2017-10-27'),
    (2, 'The Legend of Zelda: Breath of the Wild', 1, '2017-03-03'),
    (3, 'FIFA 22', 2, '2021-10-01');

INSERT INTO games (title, genre, release_date, id_console) VALUES
    ('Grand Theft Auto V', 'Ação', '2013-09-17', 1),
    ('Red Dead Redemption 2', 'Ação e Aventura', '2018-10-26', 2),
    ('The Witcher 3: Wild Hunt', 'RPG', '2015-05-19', 3);

INSERT INTO company (name, country) VALUES
    ('RockStar', 'EUA'),
    ('EA Sports', 'EUA'),
    ('CD Projekt Red', 'Polônia');
