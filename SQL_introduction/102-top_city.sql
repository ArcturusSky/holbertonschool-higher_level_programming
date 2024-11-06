-- Script that display the top 3 of cities temperature during JULY and AUGUST
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER by avg_temp DESC
LIMIT 3;