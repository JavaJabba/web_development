DROP TABLE IF EXISTS gigs;

CREATE TABLE gigs
(
    gig_id integer PRIMARY KEY AUTOINCREMENT,
    band TEXT NOT NULL,
    gig_date TEXT NOT NULL
);

INSERT IN gigs (band, gig_date)
VALUES ('Decaying Shroom', '2022-02-12'),
       ('Belated Tonic', '2022-01-21'),
       ('Belated Tonic', '2022-01-21'),       
