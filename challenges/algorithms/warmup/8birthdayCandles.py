"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem

return count of max value in a list
"""
#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    biggest = max(ar)
    count = 0
    for i in ar:
        if i == biggest:
            count += 1

    return(count)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
