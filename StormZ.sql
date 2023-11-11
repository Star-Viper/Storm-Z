CREATE DATABASE StormZ;

USE StormZ;

CREATE TABLE User (
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Gender VARCHAR(10),
    ProductName VARCHAR(255),
    TotalProductPrice DECIMAL(10, 2)
);
select * from User;