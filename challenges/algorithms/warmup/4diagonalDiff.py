"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

2D arrays.
Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15
"""

                                                                #!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    firstSum = 0 #init returned difference
    secondSum = 0
    for i in range(len(a)):
        firstSum += a[i][i]
        secondSum += a[i][len(a)-1-i] #would be more efficient if size passed in

    return abs(firstSum - secondSum)

#given:
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
