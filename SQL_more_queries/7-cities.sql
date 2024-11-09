-- Script that creates the database "hbtn_0d_usa" and the table "cities"
-- (in the database "hbtn_0d_usa") on my MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to work in for the table creation
USE hbtn_0d_usa;

-- Note: If Primary Key, UNIQUE isn't required
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL 
);