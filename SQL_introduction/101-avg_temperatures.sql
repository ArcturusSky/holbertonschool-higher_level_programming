-- Script that display the average temperature (Fahrenheit) by city ordered by temps
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER by avg_temp DESC;