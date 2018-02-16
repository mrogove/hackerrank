/*
Query the list of CITY names from STATION that do not
  start with vowels and do not end with vowels.
Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) not in ('a','e','i','o','u')
	AND SUBSTRING(CITY,1,1) not in ('a','e','i','o','u');
