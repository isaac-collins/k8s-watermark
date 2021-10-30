CREATE DATABASE images;
USE images;
CREATE TABLE images 
(
    id INT NOT NULL AUTO_INCREMENT,
    timestamp VARCHAR(50),
    data VARCHAR(255),
    PRIMARY KEY ( id )

);
INSERT INTO images 
(
    timestamp,
    data
)
VALUES
(
    "ts",
    "data"
);