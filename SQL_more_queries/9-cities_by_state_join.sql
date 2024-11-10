-- Script that lists all cities along with their corresponding state names
SELECT cities.id, cities.name, states.name   -- Selecting city ID, city name, and state name to be displayed
FROM cities
INNER JOIN states                            -- Joining the "states" table to get state info
ON cities.state_id = states.id               -- Matching "cities' state_id" to "states' id"
ORDER BY cities.id ASC;                      -- Sorting the results by city ID in ascending order
