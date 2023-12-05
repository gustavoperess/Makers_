-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year) VALUES ('Doolittle', 1989);
INSERT INTO albums (title, release_year) VALUES ('Surfer Rosa', 1988);
INSERT INTO albums (title, release_year) VALUES ('Waterloo', 1972);
INSERT INTO albums (title, release_year) VALUES ('Bossanova', 1990);
INSERT INTO albums (title, release_year) VALUES ('Lover', 2019);
