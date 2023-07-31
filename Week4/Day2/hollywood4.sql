-- Create country table 
-- one - to - many 

-- create table country (
-- id smallserial primary key, 
-- name varchar(50) not null, 
-- country_code smallint not null check(country_code < 50)
-- ); 

-- FOREIGN KEY (country_id) REFERENCES country(id); 

-- 1 - add a new column
-- alter table actors 
-- add column country_id smallint; 

-- 2 - specify the new column as foreign key
-- alter table actors
-- add foreign key (country_id) references country(id);

-- insert into country (name, country_code) 
-- values
-- ('USA', 40);

-- insert into country (name, country_code) 
-- values
-- ('France', 33),
-- ('Britain', 20);


-- actors -> country

-- update actors set country_id = 2 where first_name = 'Matt';
-- update actors set country_id = (select id from country where name = 'USA') where first_name in ('George', 'Brad', 'Patrick', 'Marc', 'Yoan', 'Lea', 'Amelia', 'David', 'Omer');
-- update actors set country_id = (select id from country where name = 'USA') where actor_id =3;

