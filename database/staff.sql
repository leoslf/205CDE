# vim: ft=mysql

USE 205CDE_Project;

CREATE TABLE staff (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(255)
    role ENUM("user","manager","admin","") NOT NULL DEFAULT "user"
);

