-- actors (country_id) -> country (id)

select actors.first_name, actors.last_name, country.name
from actors
join country
on actors.country_id = country.id
where actors.first_name != 'Matt'
order by actors.first_name;