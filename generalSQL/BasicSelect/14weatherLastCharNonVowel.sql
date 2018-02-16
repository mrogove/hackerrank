/*
Query the list of CITY names from STATION that do not end with vowels.
Your result cannot contain duplicates.
  mysql-compatible
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) not in ('a','e','i','o','u');
