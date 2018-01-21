"""
Print a single base-10 integer n denoting the maximum number
of consecutive 1's in the binary representation of N.
"""
#!/bin/python3

import sys

def intToBinary(num):
    bin1 = str(bin(num))[2:]
    return bin1

def countAdjacentChars(stringVal):
    maxCount1s = len(max(list(stringVal.split('0'))))
    return maxCount1s

n = int(input().strip())
n = intToBinary(n)
countAdjacent = countAdjacentChars(n)
print(countAdjacent)
