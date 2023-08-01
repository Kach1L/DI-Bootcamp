-- Table: public.puzzle

-- DROP TABLE IF EXISTS public.puzzle;

-- CREATE TABLE IF NOT EXISTS public.puzzle
-- (
-- 

-- TABLESPACE pg_default;

-- ALTER TABLE IF EXISTS public.puzzle
--     OWNER to postgres;

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab


-- Q1
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL)
-- It prints the count of FirstTab id that does not equal to null. All firstTab rows execpt for NULL row.


-- Q2
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- It prints the FirstTab item that has the SecondTab id of 5. All firstTab rows execpt for '5' row.


-- Q3
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- It prints the FirstTab item that doesn't have a SecondTab id. All firstTab rows execpt for rows with secondTab ids.

-- Q4
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- It prints the FirstTab item that doesn't have the SecondTab id of NULL. All firstTab rows execpt for '5' row. Only prints NULL row.	