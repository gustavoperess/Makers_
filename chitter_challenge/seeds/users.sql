DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    user_password VARCHAR(255)
);


INSERT INTO users (user_name, user_password) VALUES ('Gustavo', 'Gustavo123');
INSERT INTO users (user_name, user_password) VALUES ('Ashley', 'Ashley123');