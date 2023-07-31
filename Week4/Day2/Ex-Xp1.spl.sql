-- CREATE TABLE items(
--    id serial primary key,
--    utility text,
--    price integer
-- );

-- INSERT INTO items (id, utility, price)
-- VALUES
-- (1, 'Small Desk', 100),
-- (2, 'Large desk', 300),
-- (3, 'Fan', 80);

-- SELECT * FROM items;
-- SELECT * FROM items ORDER by price;
-- SELECT * FROM items where price >= 80 order by price DESC;



-- CREATE TABLE customers(
--    id serial PRIMARY KEY,
--    fname varchar(50),
--    lname varchar(50)
-- );

-- INSERT INTO customers (fname, lname)
-- VALUES
-- ('GregSandraScott', 'Jones'),
-- ('SandraScott', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'MelanieGreen'),
-- ('Melanie', 'Johnson');

-- ALTER TABLE customers
-- DROP PRIMARY KEY;

-- SELECT * FROM customers;
-- SELECT * FROM customers WHERE lname = 'Smith';
-- SELECT fname, lname FROM customers order by fname DESC;
-- SELECT lname FROM customers order by lname DESC;
