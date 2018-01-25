"""
https://www.hackerrank.com/challenges/plus-minus/problem
Given an array of integers, calculate which fraction of its elements are positive,
which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively.

Print the decimal value of each fraction on a new line.

Sample Input

6
-4 3 -9 0 4 1

Sample Output

0.500000
0.333333
0.166667
"""

#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    # not particularly "pythonic". also neglected formatting. But is accurate.
    total = len(arr)
    countPos = 0
    countNeg = 0
    countZero = 0
    for i in arr:
        if i > 0:
            countPos += 1
        elif i < 0:
            countNeg += 1
        else:
            countZero += 1

    print(countPos/total)
    print(countNeg/total)
    print(countZero/total)

#given this:
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
