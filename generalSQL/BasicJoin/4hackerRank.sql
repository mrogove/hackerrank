/*
show hackers that score maximum on >1 challenge
meant to be mySQL compatible; compiler on hackerrank not cooperating
https://www.hackerrank.com/challenges/full-score/problem
*/

SELECT h.hacker_id
    ,  h.name
FROM Challenges c
INNER JOIN Submissions s
  ON s.challenge_id = c.challenge_id
INNER JOIN Hackers h
  ON h.hacker_id = c.hacker_id
INNER JOIN Difficulty d
  ON c.difficulty_level = d.difficulty_level
WHERE d.score = s.score
  and d.difficulty_level = c.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.hacker_id)>1
ORDER BY COUNT(s.hacker_id) desc, s.hacker_id
