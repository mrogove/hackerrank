"""
simplearraysum
https://www.hackerrank.com/challenges/simple-array-sum/problem
Given an array of N integers, can you find the sum of its elements?
"""
#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    res = 0 #init
    for x in ar:
        res += x
    return res


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
