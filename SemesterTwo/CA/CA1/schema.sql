CREATE TABLE Players
(
    player_id varchar(255) PRIMARY KEY NOT NULL,
    password varchar(255),
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    date_joined DATE NOT NULL,
    date_due DATE
);

CREATE TABLE Games
(
    game_name varchar(255) PRIMARY KEY NOT NULL,
    game_type varchar(255) NOT NULL,
    manufacturer varchar(255) NOT NULL
);

CREATE TABLE PlayerGameRelation
(
    player_id varchar(255) NOT NULL,
    game_name varchar(255) NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id),
    FOREIGN KEY (game_name) REFERENCES Games(game_name),
    UNIQUE (player_id, game_name)
);   


CREATE TABLE Faction
(
    faction_name varchar(255) PRIMARY KEY NOT NULL,
    alliance varchar(255) NOT NULL
);

CREATE TABLE FactionGameRelation
(
    faction_name varchar(255) NOT NULL,
    game_name varchar(255) NOT NULL,
    FOREIGN KEY (faction_name) REFERENCES Faction(faction_name),
    FOREIGN KEY (game_name) REFERENCES Games(game_name),
    UNIQUE (faction_name, game_name)
);   

CREATE TABLE PlayerFactionRelation
(
    player_id varchar(255) NOT NULL,
    faction_name varchar(255) NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id),
    FOREIGN KEY (faction_name) REFERENCES Faction(faction_name),
    UNIQUE (player_id, faction_name)
);   

INSERT INTO Games (game_name, game_type, manufacturer)
VALUES
    ("Warhammer: Age of Sigmar", "28mm Fantasy Wargame", "Games Workshop"),
    ("Warhammer: 40'000", "28mm Sci-Fi Wargame", "Games Workshop"),
    ("Bolt Action", "28mm Historical Wargame", "Warlord Games"),
    ("Marvel Crisis Protocol", "28mm Comic Book Skirmish Game", "Atomic Mass Games"),
    ("Gaslands", "28mm Skirmish Racing", "Planet Smasher Games"),
    ("Silver Bayonet", "28mm Historical Fiction Skirmish Game", "Osprey Publishing");

INSERT INTO Faction(faction_name, alliance)
VALUES
    ("German", "Axis"),
    ("Japanese", "Axis"),
    ("French", "Allied"),
    ("British", "Allied"),
    ("Soviet Union", "Allied"),
    ("Italian", "Axis"),
    ("Space Marines", "Imperium"),
    ("Orks", "Xenos"),
    ("World Eaters","Chaos"),
    ("Daemons", "Chaos"),
    ("Imperial Guard", "Imperium"),
    ("Sisters of Battle", "Imperium"),
    ("Drukari", "Xenos"),
    ("Orruk Warclans", "Destruction"),
    ("Orge Mawclans", "Destruction"),
    ("Stormcast Eternals", "Order"),
    ("Idoneth Deepkin", "Order"),
    ("Blades of Khorne", "Chaos"),
    ("Maggotkin of Nurgle", "Chaos"),
    ("Slaves to Darkness", "Chaos"),
    ("Lumineth Realmlords", "Order"),
    ("Tau", "Xenos"),
    ("Adeptus Mechanicus", "Imperium");

