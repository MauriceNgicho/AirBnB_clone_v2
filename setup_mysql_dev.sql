-- create tha database if it is missing
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user in local host
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';
-- grant permissions
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Select Grants on perfomance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush
FLUSH PRIVILEGES
