-- 1
-- SELECT customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active
-- FROM public.customer;

-- 2
-- SELECT (first_name, last_name) as full_name 
-- from public.customer;

-- 3
-- SELECT DISTINCT create_date 
-- from public.customer;

-- 4
-- SELECT * from customer
-- order by first_name DESC;

-- 5
-- SELECT film_id, title, description, release_year, rental_rate
-- from film order by rental_rate ASC;

-- 6
-- SELECT address, phone FROM public.address 
-- WHERE district = 'Texas';

-- 7
-- SELECT film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, last_update, special_features, fulltext
-- FROM public.film WHERE film_id = 15 or film_id = 150;

-- 8
-- SELECT film_id, title, description, length, rental_rate 
-- FROM public.film WHERE title = 'Academy Dinosaur';

-- 9
-- SELECT film_id, title, description, length, rental_rate 
-- FROM public.film WHERE title LIKE 'Ac%';

-- 10 NOT SURE OF ANSWER
-- SELECT payment_id, customer_id, staff_id, rental_id, amount, payment_date FROM public.payment
-- WHERE amount < 0.01 
-- LIMIT 10;

-- 11
-- SELECT payment_id, customer_id, staff_id, rental_id, amount, payment_date FROM public.payment
-- WHERE amount < 0.01 
-- LIMIT 20;

-- 12 NOT SURE OF ANSWER
-- SELECT customer.first_name, customer.first_name, payment.amount, payment.payment_date 
-- From customers
-- INNER JOIN payment ON customers.paymentID=payment.paymentID;

-- 13 NOT SURE OF ANSWER
-- SELECT customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active
-- FROM public.customer WHERE inventory_id NOT IN *;

-- 14
-- SELECT city_id, city, country_id, last_update
-- 	FROM public.city WHERE city_id = country_id;

-- 15
-- SELECT customer_id, first_name, last_name
-- 	FROM public.customer;

-- B
-- SELECT amount, payment_date
-- 	FROM public.payment;




