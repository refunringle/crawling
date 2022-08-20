DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS songs;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,name VARCHAR(50)
);


CREATE TABLE songs(
    id SERIAL PRIMARY KEY,name VARCHAR(100),artist_id INTEGER references artists(id),
    lyrics TEXT
);
