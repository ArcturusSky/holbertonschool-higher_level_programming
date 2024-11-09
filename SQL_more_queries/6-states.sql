--  Script that creates the database "hbtn_0d_usa" and the table "states"
-- (in the database "hbtn_0d_usa") on my MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to work in for the table creation
USE hbtn_0d_usa;

-- Note: If Primary Key, UNIQUE isn't required
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL 
);