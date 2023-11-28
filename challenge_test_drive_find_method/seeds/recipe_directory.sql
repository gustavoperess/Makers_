DROP TABLE IF EXISTS recipe_directory;
DROP SEQUENCE IF EXISTS recipe_directory_id_seq;


CREATE SEQUENCE IF NOT EXISTS recipe_directory_id_seq;
CREATE TABLE recipe_directory (
    id SERIAL PRIMARY KEY,
    name text,
    time int,
    rating int
);


INSERT INTO recipe_directory (name, time,  rating) VALUES ('Pasta', 1012 , 5);
INSERT INTO recipe_directory (name, time,  rating) VALUES ('Sushi', 535, 5);
INSERT INTO recipe_directory (name, time,  rating) VALUES ('Pizza', 1515, 4);
INSERT INTO recipe_directory (name, time,  rating) VALUES ('Poutine', 330, 3);
INSERT INTO recipe_directory (name, time,  rating) VALUES ('Donner', 700, 4);