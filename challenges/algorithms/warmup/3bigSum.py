"""
https://www.hackerrank.com/challenges/a-very-big-sum/problem

You are given an array of integers of size N.
You need to print the sum of the elements in the array,
keeping in mind that some of those integers may be quite large.

actually this appears to be an exact copy of problem 1 - array sum.
Python will be able to handle the values assumed:
1 <= N <=10
0 <= A[i] <= 10^10

because python infers data type
"""
import sys

def arraySum(n, ar):
    res = 0 #init
    for x in ar:
        res += x
    return(res)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = arraySum(n, ar)
print(result)
