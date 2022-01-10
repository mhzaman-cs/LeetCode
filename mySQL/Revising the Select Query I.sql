-- Weather Observation Station 8 (EASY) https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT DISTINCT CITY from STATION WHERE RIGHT(CITY, 1) in ("a", "e", "i", "o", "u") AND LEFT(CITY, 1) in ("a", "e", "i", "o", "u");

-- Weather Observation Station 7 (EASY) https://www.hackerrank.com/challenges/weather-observation-station-7/problem
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ("a", "e", "i", "o", "u");

-- Country Code (EASY) https://www.hackerrank.com/challenges/revising-the-select-query/problem
SELECT * FROM CITY WHERE COUNTRYCODE = "USA" and POPULATION > 100000;
