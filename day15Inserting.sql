-- CRUD on SQL
UPDATE movies
SET director = "John Lasseter"
WHERE title = "A Bug's Life";

UPDATE movies
SET year = 1999
WHERE title = "Toy Story 2";

UPDATE movies
SET director = "Lee Unkrich",title = "Toy Story 3"
WHERE title = "Toy Story 8";


-- Delete, first select and then delete
SELECT * FROM movies
where year<2005;
--Then Delete
Delete FROM movies
where year<2005;

--Select first
select * FROM movies
where director like "Andrew Stanton";
-- Delete
delete FROM movies
where director like "Andrew Stanton";


-- Creating a table
CREATE TABLE Database (
    name TEXT PRIMARY KEY,
    version float,
    Download_count INTEGER
);

-- Altering The Table
ALTER TABLE movies
ADD Language Text
    DEFAULT "English";