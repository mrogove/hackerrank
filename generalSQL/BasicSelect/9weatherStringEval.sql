/*
  https://www.hackerrank.com/challenges/weather-observation-station-5/problem
  Query the two cities in STATION with the shortest and longest CITY names,
  as well as their respective lengths (i.e.: number of characters in the name).
  If there is more than one smallest or largest city,
  choose the one that comes first when ordered alphabetically.
*/

Select top 1 city, len(city)
from Station
where Len(City) = (SELECT Min(Len(City))FROM station)
order by city;

Select top 1 city, len(city)
from Station
where Len(City) = (SELECT Max(Len(City))FROM station)
order by city;
