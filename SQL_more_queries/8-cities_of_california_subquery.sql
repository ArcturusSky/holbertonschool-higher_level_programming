-- Script that lists all the cities of California that can be found in the database "hbtn_0d_usa".

-- Retrieve cities where state_id matches California's state_id
SELECT cities.id, cities.name FROM cities 
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;
