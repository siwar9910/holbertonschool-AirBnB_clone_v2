-- script that prepares a MySQL server for the project
-- create test db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user if he doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- set a password for the user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- grant the privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select the  privileges to the user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush the privileges
FLUSH PRIVILEGES;
