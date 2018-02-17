/**
Given the CITY and COUNTRY tables, query the names of all cities
where the CONTINENT is 'Africa'.
**/

SELECT DISTINCT city.name
FROM city
INNER JOIN country
  ON city.CountryCode = country.Code
WHERE country.CONTINENT = 'Africa'
