DROP TABLE IF EXISTS Players;

CREATE TABLE Players(
    player_id varchar(255) PRIMARY KEY NOT NULL,
    password varchar(255),
    highscore INT DEFAULT 0
);