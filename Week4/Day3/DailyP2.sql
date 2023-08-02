-- Part2 1
-- CREATE TABLE Book(
-- book_id SERIAL PRIMARY KEY,
-- title varchar(50) NOT NULL,
-- author varchar(50) NOT NULL
-- );

-- Part2 2
-- INSERT INTO Book (title,author)
-- VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- Part2 3
-- CREATE TABLE Student(
-- student_id SERIAL PRIMARY KEY,
-- name varchar(50) NOT NULL UNIQUE,
-- age INTEGER CHECK(age BETWEEN 1 and 15)
-- );

-- Part2 4
-- INSERT INTO Student (name,age)
-- VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- Part2 5
-- CREATE TABLE Library(
-- book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- borrowed_date date
-- );



-- Part2 6
-- SELECT * FROM Book;
-- SELECT * FROM Student;

-- INSERT INTO Library (student_fk_id,book_fk_id,borrowed_date)
-- VALUES
-- ((SELECT student_id FROM Student WHERE name = 'John'),(SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),'15/02/2022'),
-- ((SELECT student_id FROM Student WHERE name = 'Bob'),(SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),'03/03/2021'),
-- ((SELECT student_id FROM Student WHERE name = 'Lera'),(SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),'23/05/2021'),
-- ((SELECT student_id FROM Student WHERE name = 'Bob'),(SELECT book_id FROM Book WHERE title = 'Harry Potter'),'12/08/2021');


-- Part2 7
-- A
-- SELECT * FROM Library;

-- B
-- SELECT name,title FROM Library
-- INNER JOIN Student ON Student.student_id = Library.student_fk_id
-- INNER JOIN Book ON Book.book_id = Library.book_fk_id
-- WHERE borrowed_date IS NOT null;

-- C
-- SELECT AVG(age) FROM Library
-- INNER JOIN Student ON Student.student_id = Library.student_fk_id
-- INNER JOIN Book ON Book.book_id = Library.book_fk_id
-- WHERE title = 'Alice in Wonderland'

-- D
-- DELETE FROM Student
-- WHERE name = 'John'
-- SELECT * FROM Library
-- Library lost one of its student_id's.