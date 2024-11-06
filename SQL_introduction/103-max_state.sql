-- Script that display the max temp of each state ordered by state name
SELECT state, max(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER by max_temp DESC;