SELECT name,role FROM employees
    where building is null;



--Second one
select distinct building_name from buildings
left join employees
on buildings.building_name = empployees.building
where role is null


SELECT distinct title, (Domestic_sales + International_sales)/1000000 as combine FROM movies
    left join boxoffice
    on id = movie_id;

SELECT title,rating*10 FROM movies
    left join boxoffice
    on id = movie_id;

SELECT * FROM movies
    where year% 2 = 0;


SELECT max(	Years_employed) FROM employees;


SELECT role,avg(Years_employed) FROM employees
    group by role ;

SELECT building,sum(Years_employed) FROM employees
    group by building ;

SELECT count() FROM employees
    where role like "artist";

SELECT role,count() FROM employees
    group by role;

SELECT sum(Years_employed) FROM employees
    group by role having role like "Engineer";

SELECT director,count() FROM movies
    group by director;

SELECT director,sum(Domestic_sales + International_sales) FROM movies
    left join boxoffice on id = movie_id
    group by director;