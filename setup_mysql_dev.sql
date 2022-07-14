-- prepares a MySQL server for the project
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user if he doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- set a password for the user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- grant the privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select the privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush the privileges
FLUSH PRIVILEGES;
