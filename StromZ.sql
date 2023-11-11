CREATE DATABASE StormZ;

USE StormZ;

CREATE TABLE IF NOT EXISTS selected_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    action_type ENUM('add', 'delete') NOT NULL,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM selected_products;
