"""
https://www.hackerrank.com/challenges/kangaroo/problem

x1,v1,x2,v2

x indicates starting position, v indicates distance for each jump

If they will ever land at same point at same time (i.e. have least common multiple and share y)
then print yes, else no

pointed out in forums: solve this eq: x1 + y * v1 = x2 + y * v2 where y = # of jumps
so:
(x1-x2)%(v2-v1)==0 then they meet.

problem states x2 is greater than x1
"""

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v2 == v1:
        return "NO"
    elif ((x1-x2) % (v2-v1) == 0) and (v2<v1):
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
