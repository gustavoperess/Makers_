-- Below is the table for testing purpose

-- Drop tables and sequences if they exist
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Create sequence for users
CREATE SEQUENCE users_id_seq;

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE,
    user_password VARCHAR(255)
);

-- Create sequence for posts
CREATE SEQUENCE posts_id_seq;

-- Create posts table with a foreign key constraint
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title VARCHAR(255),
    post_content VARCHAR(255),
    post_number_of_views INT,  
    
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES users (id)
);

-- Insert sample data into users and posts tables
INSERT INTO users (user_name, user_password) VALUES ('Gustavo', 'Gustavo123');
INSERT INTO users (user_name, user_password) VALUES ('Ashley', 'Ashley123');
INSERT INTO users (user_name, user_password) VALUES ('Mario', 'Mario123');
INSERT INTO users (user_name, user_password) VALUES ('Rosangela', 'Rosangela123');
INSERT INTO posts (post_title, post_content, post_number_of_views, user_id) VALUES ('title01', 'content01', 145, 1);
INSERT INTO posts (post_title, post_content, post_number_of_views, user_id) VALUES ('title02', 'content02', 245, 1);
INSERT INTO posts (post_title, post_content, post_number_of_views, user_id) VALUES ('title03', 'content03', 45, 2);
