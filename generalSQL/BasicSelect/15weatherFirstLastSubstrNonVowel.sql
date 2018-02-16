/*
Query the list of CITY names from STATION that either do not start
  with vowels or do not end with vowels.
Your result cannot contain duplicates.
note - or
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) not in ('a','e','i','o','u')
	OR SUBSTRING(CITY,1,1) not in ('a','e','i','o','u');
