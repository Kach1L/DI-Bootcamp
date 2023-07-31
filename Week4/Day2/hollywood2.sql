-- 1. Create another table producers, with a foreign key : the id of a country. 
-- 2. create movies_producers table, which will have 2 foreign keys - producer_id, movie_id
-- 2. Insert some records 
-- 3. Display with INNER JOIN <- not mandatory

-- Good Will Hunting - Lawrence Bender
-- Jason Bourne - Frank Marshall

-- 1
-- create table producers (
-- id serial primary key, 
-- name varchar(50) unique, 
-- country_id smallint references country(id)); 

-- 2
-- create table movies_producers (
-- id serial primary key, 
-- producer_id int references producers(id),
-- movie_id int references movie(id)
-- );

-- insert into producers(name, country_id)
-- values 
-- ('Lawrence Bender', (select id from country where name = 'USA')),
-- ('Frank Marshall', (select id from country where name = 'USA'));


-- 3
-- insert into movies_producers (producer_id, movie_id)
-- values
-- ((select id from producers where name = 'Frank Marshall'), (select id from movie where title = 'Jason Bourne')), 
-- ((select id from producers where name = 'Frank Marshall'), (select id from movie where title = 'Oceans 8')), 
-- ((select id from producers where name = 'Lawrence Bender'), (select id from movie where title = 'Good Will Hunting'));

-- 4 
-- movie <-> movies_producers
-- producers <-> movies_producers
select movie.title, producers.name
from movie
inner join movies_producers on movie.id = movies_producers.movie_id
inner join producers on producers.id = movies_producers.producer_id;