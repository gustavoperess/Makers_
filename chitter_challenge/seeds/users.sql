DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE users_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE,
    user_password VARCHAR(255)
);

CREATE SEQUENCE users_chitters_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title VARCHAR(255),
    post_content VARCHAR(255),
    post_number_of_views int,
    
    user_id int,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES users (id)
);
