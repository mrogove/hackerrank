"""
https://www.hackerrank.com/challenges/between-two-sets/problem
all elements in A are a factor of x
x is a factor of all elements in B
so x mod ai = 0 for all a
and bi mod x = 0 for all b

The first line contains two space-separated integers describing the respective values of
    (the number of elements in set A) and (the number of elements in set B).
The second line contains distinct space-separated integers describing a0,a1,etc.
The third line contains distinct space-separated integers describing b0,b1,etc.
Sample Input

2 3
2 4
16 32 96

Sample Output

3
(e.g. 4, 8)


"""
#!/bin/python3

import sys
from fractions import gcd
from functools import reduce

def getTotalX(a, b):
    #find LCM of a
    lcm = a[0] #init
    for i in a[1:]: #starting at next value
        lcm = lcm*i/gcd(lcm, i) #compare adjacent values; multiple/gcd of two values
    #LCM of a[] has been found
    #determine GCD
    gcdVal = reduce(gcd,b) #returns value from function on iterator, b
    #GCD of b[] has been found, so:
    count = 0
    lcmVal = lcm
    while lcmVal <= gcdVal:
        if(gcdVal % lcmVal) == 0:
            count+=1
        lcmVal = lcmVal + lcm #keep adding the LCM to compare
    return(count)

###given:
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
