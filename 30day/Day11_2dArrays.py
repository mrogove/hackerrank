"""hourglass defined as:
[i][j],[i][j+1],[i][j+2]
[i+1][j+1]
[i+2][j],[i+2][j+1],[i+2][j+2]
how to deal with out of range? limit i and j to always be < (len-2)

https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""
#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

allVals = []
for i in range(len(arr)-2):
    for j in range(len(arr[0])-2):
        sumval = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        allVals.append(sumval)
print(max(allVals))
