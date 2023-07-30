-- CREATE TABLE students(
--    id serial primary key,
--    fname text,
--    lname text,
--    birth_date date
-- );

-- INSERT INTO students (fname, lname, birth_date)
-- VALUES
-- ('Marc', 'Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson', '03/10/1980');

-- SELECT * FROM students;
-- SELECT fname, lname FROM students;
-- SELECT fname, lname FROM students WHERE id = 2;
-- SELECT fname, lname FROM students WHERE lname = 'Benichou' OR fname = 'Marc';
-- SELECT fname FROM students WHERE fname LIKE '%a%';
-- SELECT fname FROM students WHERE fname LIKE 'A%';
-- SELECT fname FROM students WHERE fname LIKE '%a';
-- SELECT fname FROM students WHERE fname LIKE '%a_';
-- SELECT * FROM students WHERE id = 1 OR id = 3;




-- DAILY CHALLENGE


-- CREATE TABLE actors(
--    id serial primary key,
--    fname text,
--    lname text,
--    birth_date date
-- );

-- INSERT INTO actors (fname, lname, birth_date)
-- VALUES
('Marc', 'Benichou', '02/11/1998'),
('Yoan', 'Cohen', '03/12/2010'),
('Lea', 'Benichou', '27/07/1987'),
('Amelia', 'Dux', '07/04/1996'),
('David', 'Grez', '14/06/2003'),
('Omer', 'Simpson', '03/10/1980'),
('', '', '01/01/1010');

-- SELECT * FROM actors;
-- SELECT *, COUNT(actors) AS actors FROM actors GROUP BY actors.id;
