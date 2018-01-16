"""
https://www.hackerrank.com/challenges/30-loops/problem

Given integer, n (2<=n<=20), print first 10 multiples.

Sample Input

2

Sample Output

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

easy
"""
import sys

n = int(input().strip())

i = 1 #initialize at 1; not 0

for i in range(1,11):
    print(str(n) + ' x ' + str(i) + ' = ' + str(n*i))
