-- CREATE DATABASE IF NOT EXISTS openai;
-- use openai;


CREATE TABLE IF NOT EXISTS books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    hero VARCHAR(2000) NOT NULL,
    summary VARCHAR(2000) NOT NULL
);

CREATE TABLE IF NOT EXISTS books_details(
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    seq INT NOT NULL,
    content VARCHAR(2000) NOT NULL,
    image_url VARCHAR(1000) NOT NULL
);

CREATE TABLE IF NOT EXISTS books_histories(
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    seq INT NOT NULL,
    candidate_num INT NOT NULL,
    content VARCHAR(2000) NOT NULL
);
