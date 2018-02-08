/*
	Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
	Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY 
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) in ('a','e','i','o','u');