"""
every student gets a grade

Any grade <40 is failing

Professor Sam wants to round up to next multiple of 5 IF diff < 3 (e.g. 88 -> 90; 87 -> 87)
Do not round failing grades.

assume 1 <= n <= 60
assume 0 <= grade <= 100
"""

#!/bin/python3

import sys

fail = 40 #definte this constant first - in case failure benchmark changes.

def solve(grades):
    # Complete this function
    result = []
    for e in grades:
        d = (e // 5 + 1) * 5 #how many times does it guzinta? (plus next multiple)
        if ((d - e) < 3) and (d >= fail):
            e = d
        result.append(e)

    return result

n = int(input().strip())

grades = []
grades_i = 0

for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)

result = solve(grades)

print ("\n".join(map(str, result)))
