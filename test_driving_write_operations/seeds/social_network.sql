DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS user_id_seq;


CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  user_email text,
  user_name text
);

INSERT INTO users (user_email, user_name) VALUES ('gustavo123@gmail.com', 'Gustavo');
INSERT INTO users (user_email, user_name) VALUES ('ashley123@gmail.com', 'Ashley');
INSERT INTO users (user_email, user_name) VALUES ('rosangela123@gmail.com', 'Rosangela');


DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS post_id_seq;


CREATE SEQUENCE IF NOT EXISTS post_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  post_title text,
  post_content text,
  post_number_of_viwes int, 
 
  
  user_id int,
  CONSTRAINT fk_user FOREIGN KEY (user_id)
    REFERENCES users (id)
);


INSERT INTO posts (post_title,post_content, post_number_of_viwes) VALUES ('title01', 'content01', 145);
INSERT INTO posts (post_title,post_content, post_number_of_viwes) VALUES ('title02', 'content02', 245);
INSERT INTO posts (post_title,post_content, post_number_of_viwes) VALUES ('title03', 'content03', 45);


