-- CREATE DATABASE IF NOT EXISTS openai;
-- use openai;

CREATE TABLE IF NOT EXISTS images 
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(1000) NOT NULL
);