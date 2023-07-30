create table house_expenses (
id serial primary key, 
date_paid date, 
electricity float,
water float, 
paid_by varchar(50)
);

insert into house_expenses (date_paid, electricity, water, paid_by) 
values 
('2005-02-11', 56.5, 20.2, 'Adam'),
('2005-03-12', 60.5, 18.2, 'Yossi'),
('2005-04-13', 70.5, 28.2, 'Yossi'),
('2005-05-14', 65.5, 26.2, 'Adam'),
('2005-06-15', 40.5, 10.2, 'Yossi'); 

-- select * from house_expenses;
-- select electricity from house_expenses;
-- select electricity, water from house_expenses;


-- select * from house_expenses where id = 1 or id = 2;
-- select * from house_expenses where id < 3;
-- select * from house_expenses where id in (1, 2);\


-- select paid_by, sum(electricity + water), max(electricity + water)
-- from house_expenses where electricity > 40
-- group by paid_by

-- update house_expenses
-- set date_paid = '2005-02-11'
-- where id = 3;

-- update house_expenses
-- set water = '20.9'
-- where id = 1;

-- delete from house_expenses where electricity < 40;
-- select * from house_expenses;

-- TRUNCATE TABLE house_expenses RESTART IDENTITY;


