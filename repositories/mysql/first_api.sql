CREATE DATABASE IF NOT EXISTS first_api;

USE first_api;

CREATE TABLE users (
    userName varchar(255) not null,
    userPassword varchar(255) not null,
    clientSecret varchar(255) not null
);

INSERT INTO users (
    userName, 
    userPassword,
    clientSecret
    ) 
VALUES ( 
    'samsumg', 
    '6be00ce921e80deb2734dc892231ce22ed6d13738f8ca5455676fd3b6904e27e',
    ''
);

CREATE TABLE basic (
    accountId varchar(255) not null,
    day varchar(255) not null,
    campaignName varchar(255) not null,
    campaignID varchar(255) not null,
    adName varchar(255) not null,
    adID varchar(255) not null,
    impressions int,
    clicks int,
    spend float
);

-- INSERT INTO basic (
--     accountId,
--     campaignName,
--     campaignID,
--     adName,
--     adID,
--     impressions,
--     clicks,
--     spend
--     ) 
-- VALUES (
--     2456123452365
--     'campanha1', 
--     '123456', 
--     'adName1',
--     '987654',
--     '3242',
--     '454',
--     '15000'
-- );