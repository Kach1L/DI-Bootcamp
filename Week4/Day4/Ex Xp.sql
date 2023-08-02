-- SELECT language_id, name, last_update
-- 	FROM public.language;

-- EX1 1
-- SELECT name
-- FROM public.language;


-- EX1 2
-- A
-- ALTER TABLE public.film
-- ADD language_ident INTEGER REFERENCES film(film_id)

-- SELECT title, description, name
-- FROM film
-- RIGHT JOIN public.language ON film.language_id=language.language_id

-- B
-- ALTER TABLE public.language
-- ADD film_ident INTEGER REFERENCES language(language_id)

-- SELECT name, description, title
-- FROM language
-- LEFT JOIN public.film ON language.film_ident=film.film_id


-- EX1 3
-- CREATE TABLE new_film(
-- id serial PRIMARY KEY,
-- name varchar(50)
-- );

-- INSERT INTO new_film (name)
-- VALUES
-- ('Jurassic Park'),
-- ('Casa Solo'),
-- ('Oppenheimer'),
-- ('Stranger Things'),
-- ('Jurassic Park');


-- EX1 4
-- CREATE TABLE customer_review(
-- review_id serial NOT NULL PRIMARY KEY,
-- film_id INTEGER References new_film(id) ON DELETE CASCADE,
-- language_id INTEGER References language(language_id),
-- title varchar(50),
-- score smallint CHECK(score between 1 and 10) NOT NULL,
-- review_text text,
-- last_update date DEFAULT NOW()
-- );


-- INSERT INTO customer_review (film_id,language_id,title,score,review_text,last_update)
-- VALUES
-- ((SELECT id FROM new_film WHERE name = 'Jurassic Park'), (SELECT language_id FROM language WHERE name = 'English'), 'Good Movie', 7, 'It was a pretty good movie. Action packed and breath-taking.', DEFAULT),
-- ((SELECT id FROM new_film WHERE name = 'Casa Solo'), (SELECT language_id FROM language WHERE name = 'Italian'), 'Great Movie', 9, 'It was a pretty great movie. Really worth its money', DEFAULT);

-- DELETE FROM new_film WHERE name = 'Jurassic Park';
-- DELETE FROM customer_review  WHERE review_id > 2;

-- SELECT * FROM new_film;


-- EX2 1
-- SELECT language_id, name, last_update, film_ident
-- 	FROM public.language;

-- UPDATE language
-- SET name = 'Swedish'
-- WHERE language_id = 6;

-- UPDATE language
-- SET name = 'Chinese'
-- WHERE language_id = 3;

-- SELECT language_id, name, last_update, film_ident
-- 	FROM public.language;


-- EX2 2 NOT SURE
-- The foreign keys are store_id. We do a sub-query that will print the id of the store table for each value iteration.


-- EX2 3
-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- DROP TABLE customer_review;
-- It is an easy step, and doesn't need extra checking.


-- EX2 4
-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- SELECT COUNT(*) FROM rental; --16044
-- counting all the rows in the table
-- SELECT COUNT(return_date) FROM rental; --15861
-- COUNT ONLY THE ROWS 
-- where this column is not null

-- EX2 5
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- SELECT title
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
-- ORDER BY replacement_cost DESC
-- LIMIT 30


-- EX2 6 - The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT title, decription, fulltext
-- FROM film
-- INNER JOIN film_actor AS fa ON film.film_id = film_actor.film_id
-- INNER JOIN actor ON actor.actor_id = fa.actor_id
-- WHERE description ILIKE '%sumo wrestler%'
-- AND first_name ILIKE '%penelope%'
-- AND last_name ILIKE '%monroe%'

-- Method 2
-- SELECT title
-- FROM film
-- WHERE fulltext @@tsquery('sumo') and fulltext @@tsquery('wrestler')

-- EX2 6 Part2 - The 2nd film : A short documentary (less than 1 hour long), rated "R".
-- SELECT title, category.name, film.length
-- FROM film
-- INNER JOIN film_category AS fc ON film.film_id = fc.film_id
-- INNER JOIN category ON category.category_id = fc.category_id
-- WHERE description ILIKE '%documentary%'
-- AND film.length < 60
-- AND rating = 'R'


-- EX2 6 Part3 - The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.

-- SELECT film.title, payment.amount, customer.first_name, customer.last_name 
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN payment ON rental.rental_id = payment.rental_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE payment.amount > 4 AND
-- customer.first_name = 'Matthew' AND
-- customer.last_name = 'Mahan'
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'


-- EX2 6 Part4 - The 4th film : His friend Matthew Mahan watched this film, 
-- as well. It had the word "boat" in the title or description,
-- and it looked like it was a very expensive DVD to replace.

-- SELECT film.title, film.replacement_cost
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE 
-- customer.first_name = 'Matthew' 
-- AND
-- customer.last_name = 'Mahan'
-- AND (title ILIKE '%boat%' OR description ILIKE '%boat%')
-- ORDER BY film.replacement_cost DESC


