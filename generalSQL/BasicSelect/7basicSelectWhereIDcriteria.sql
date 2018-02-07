"""
https://www.hackerrank.com/challenges/weather-observation-station-3/problem
return city names with even IDs only
"""
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID,2) = 0;
