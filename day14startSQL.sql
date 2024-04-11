--Lesson 2

SELECT * FROM movies 
where id = 6;

-- Other Questions
SELECT * FROM movies 
    where year between 2000 and 2010;

SELECT * FROM movies 
    where year not between 2000 and 2010;

-- Last question
SELECT * FROM movies 
    where id <6;


    -- Lessom 3
    -- use % Used anywhere in a string to match a sequence of zero or more characters
    -- use - only one character.
    SELECT * FROM movies
    where title like "Toy Story%";

    SELECT * FROM movies
    where director = "John Lasseter";

    SELECT * FROM movies
    where director != "John Lasseter";

    SELECT * FROM movies
    where title like "WALL-%";


--Lesson 4
SELECT DISTINCT director FROM movies
    ORDER BY director;

SELECT * FROM movies
    order by Year Desc
    limit 4;

SELECT * FROM movies
    order by title
    limit 5;

SELECT * FROM movies
    order by Title
    limit 5 offset 5;


--Lesson 5
SELECT * FROM north_american_cities
    where country like "United States"
    order by latitude desc;

SELECT * FROM north_american_cities
    where longitude < -87.629798
    order by longitude;

SELECT * FROM north_american_cities
    where country = "Mexico"
    order by population desc
    limit 2;

SELECT City, Population FROM north_american_cities
    where country = "United States"
    order by population desc
    limit 2 offset 2;


-- Find the domestic and international sales for each movie 
SELECT * FROM movies 
    inner join Boxoffice
    on movies.id = Boxoffice.movie_id;
-- You can shorted things up
SELECT * FROM movies 
    inner join Boxoffice
    on id = movie_id;

SELECT * FROM movies 
    inner join Boxoffice
    on id = movie_id
    where International_sales > Domestic_sales;

SELECT * FROM movies 
    inner join Boxoffice
    on id = movie_id
    order by rating desc;



SELECT distinct building_name,role FROM Buildings
    left join employees
    on Buildings.building_name = Employees.building;