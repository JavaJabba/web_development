CREATE TABLE Players
(
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    date_joined DATE NOT NULL,
    date_due NOT NULL
);

CREATE TABLE Games
(
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name varchar(255) NOT NULL,
    game_type varchar(255) NOT NULL,
    manufacturer varchar(255) NOT NULL
);

CREATE TABLE PlayerGameRelation
(
    player_id INTEGER NOT NULL,
    game_id INT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id),
    UNIQUE (player_id, game_id)
);   


CREATE TABLE Faction
(
    faction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    faction_name varchar(255) NOT NULL,
    alliance varchar(255) NOT NULL
);

CREATE TABLE FactionGameRelation
(
    faction_id INT NOT NULL,
    game_id INT NOT NULL,
    FOREIGN KEY (faction_id) REFERENCES Faction(faction_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id),
    UNIQUE (faction_id, game_id)
);   

CREATE TABLE PlayerFactionRelation
(
    player_id INT NOT NULL,
    faction_id INT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id),
    FOREIGN KEY (faction_id) REFERENCES Faction(faction_id),
    UNIQUE (player_id, faction_id)
);   

INSERT INTO Players (first_name, last_name, date_joined, date_due)
VALUES
    ("Dylan", "Murray", '2017-05-15', '2022-07-28'),
    ("Jason", "Lynch", '2017-05-15', '2022-06-06'),
    ("Conor", "Considine", '2017-07-04', '2022-08-12'),
    ("Bryan", "Considine", '2017-07-04', '2022-02-12'),
    ("Sam", "Smith", '2022-02-14', '2022-08-14');

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

