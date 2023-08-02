-- Part1 1
-- CREATE TABLE Customer(
-- id SERIAL PRIMARY KEY,
-- first_name varchar(50) NOT NULL,
-- last_name varchar(50) NOT NULL
-- );

-- CREATE TABLE Customer_profile(
-- id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INTEGER UNIQUE REFERENCES Customer(id)
-- );

-- DROP TABLE Customer_profile;

-- CREATE TABLE Customer_profile(
-- id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INTEGER UNIQUE REFERENCES Customer(id)
-- );

-- Part1 2
-- INSERT INTO Customer (first_name, last_name)
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- Part1 3
-- INSERT INTO Customer_profile (isLoggedIn, customer_id)
-- VALUES
-- ('true', (select id FROM Customer WHERE first_name = 'John')),
-- ('false', (select id FROM Customer WHERE first_name = 'Jerome'));

-- Part1 4A
-- SELECT first_name
-- FROM Customer
-- INNER JOIN Customer_profile AS Cp ON Customer.id = Cp.id
-- WHERE isLoggedIn = 'true'

-- Part1 4B
-- SELECT first_name, isLoggedIn 
-- FROM Customer
-- FULL JOIN Customer_profile AS Cp ON Customer.id = Cp.id

-- Part1 4C
-- SELECT count(first_name)
-- FROM Customer
-- RIGHT JOIN Customer_profile AS Cp ON Customer.id = Cp.id
-- WHERE isLoggedIn = 'false'
