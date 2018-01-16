"""
given two integers, l and r, print all odd numbers between l and r(inclusive)
sample input:
2
5
sample output:
3
5
"""
#!/bin/python3

import sys
import os

# Complete the function below.

def  oddNumbers(l, r):
    arr = []
    i = l
    for i in range(l,r+1):
        if i%2 != 0:
            arr.append(i)

    return(arr)


#f = open(os.environ['OUTPUT_PATH'], 'w')


_l = int(input());


_r = int(input());

res = oddNumbers(_l, _r)
for res_cur in res:
    #f.write( str(res_cur) + "\n" )
    print(str(res_cur)+"\n")
#f.close()
