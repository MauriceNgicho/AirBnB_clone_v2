-- Create test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
-- Privilages
GRANT ALL PRIVILEGES ON hbnb_test_db.* to 'hbnb_test'@'localhost'; 
-- Select Permissions
GRANT SELECT perfomance_schema.* to 'hbnb_test'@'localhost';
--Flush Privileges
FLUSH PRIVILEGES
