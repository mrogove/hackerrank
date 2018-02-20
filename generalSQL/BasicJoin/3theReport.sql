/**
given Students and Grades -
report:
Name, Grade, Mark

**/

SELECT (CASE WHEN x.grade <8 THEN NULL ELSE name END) name
  , x.grade
  , x.marks
FROM
(SELECT name, grade, marks
FROM students, grades
WHERE marks BETWEEN min_Mark AND Max_Mark) x
ORDER BY x.grade DESC, x.name, ISNULL(x.marks,-1);
