/*
	Query the list of CITY names ending starting with non-vowels from STATION.
	Your result cannot contain duplicates.
  mysql-compatible
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY,1,1) not in ('a','e','i','o','u');
