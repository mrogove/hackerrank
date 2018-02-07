"""
https://www.hackerrank.com/challenges/weather-observation-station-4/problem
find the difference between the total number of CITY entries in the table and
the number of distinct CITY entries in the table.
"""

SELECT COUNT(CITY) - COUNT(distinct city)
FROM STATION
