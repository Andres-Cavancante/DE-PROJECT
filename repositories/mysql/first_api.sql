CREATE DATABASE IF NOT EXISTS first_api;

USE first_api;

CREATE TABLE users (
    userID varchar(255) not null,
    userName varchar(255) not null,
    userPassword varchar(255) not null,
    PRIMARY KEY (userID)
);

INSERT INTO users (
    userID, 
    userName, 
    userPassword
    ) 
VALUES (
    '5ee4dded-ad12-42ab-8816-84cb79ef38b8', 
    'samsumg', 
    '6be00ce921e80deb2734dc892231ce22ed6d13738f8ca5455676fd3b6904e27e'
    );

CREATE TABLE basic (
    campaignName varchar(255) not null,
    campaignID varchar(255) not null,
    adName varchar(255) not null,
    adID varchar(255) not null
);