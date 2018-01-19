"""
prison functionality
four parameters:
int n, number of horizontal bars. indexed 1 to n
int m, number of vertical bars. indexed 1 to m
array of x integers, h, where each hi is the ID of a horizontal bar removed
array of y intevers, v, where each vi is the ID of a vertical bar removed

input:
n,
m,
integer, x, number of elements in h (removed bars)
each line of subsequent x lines (0<=i<=x) contrains integer describing h
integer, y, number of elements in v (removed bars)
each line j of m subsequent lines (0<=j<=y) contrains int describing v
array values guaranteed distinct

sample input:
3 size horizontal
3 size vertical
1 number of horizontal bars removed
2 index of horizontal bar removed
1 number of vertical bars removed
2 index of vertical bar removed

Output:
4

3
2
3
1
2
3
2
1
2

"""

#!/bin/python3

import sys
import os

# Complete the function below.

def prison(n, m, h, v):
    #in example: 3,3,2,2
    arrayN = []
    arrayM = []
    i = 0 #iters
    j = 0
    while i <= n:
        arrayN.append(i)
        i+= 1
    while j <= m:
        arrayM.append(j)
        j+= 1

    arrayN = [a for a in arrayN if a not in h]
    arrayM = [b for b in arrayM if b not in v]
    print(arrayN)
    print(arrayM)

    #looked up docs on zip function for lists:
    #thiz zip should go through every adjacent pair and compare abs difference

    if arrayN == [0]: #if every horizontal bar removed...
        maxN = n+1
    else:
        maxN = max(abs(a-b) for (a,b) in zip(arrayN[1:], arrayN[:-1]))

    if arrayM == [0]: #if every vertical bar removed...
        maxM = m+1
    else:
        maxM = max(abs(c-d) for (c,d) in zip(arrayM[1:], arrayM[:-1]))

    # print(maxN)
    # print(maxM)

    return(maxM*maxN)

if __name__ == "__main__":
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    h_cnt = 0
    h_cnt = int(input())
    h_i = 0
    h = []
    while h_i < h_cnt:
        h_item = int(input())
        h.append(h_item)
        h_i += 1
    #print(str(h) + "this is h")

    v_cnt = 0
    v_cnt = int(input())
    v_i = 0
    v = []
    while v_i < v_cnt:
        v_item = int(input())
        v.append(v_item)
        v_i += 1
    #print(str(v) + "this is v")

    res = prison(n, m, h, v);
    #f.write(str(res) + "\n")
    print(res)

    #f.close()
