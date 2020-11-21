## Код SQL

#### Код sql для создания таблиц 

CREATE TABLE toys_repair (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> toy_id INT REFERENCES toys(toy_id),
    -> issue_description VARCHAR (200)
    -> );


CREATE TABLE toys (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> toy_id INT,
    -> name VARCHAR (30),
    -> status VARCHAR (10),
    -> status_update DATE);


CREATE TABLE games (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> game_id INT,
    -> name VARCHAR (30),
    -> date DATE);

CREATE TABLE toys_games (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> game_id INT REFERENCES games(game_id),
    -> toy_id INT REFERENCES toys(toy_id),
    -> note VARCHAR (150));