"""
https://www.hackerrank.com/challenges/mini-max-sum/forum

Given 5 ints, find max and min sum of 4 of the ints

found very clever solution in forums, went with that instead
of trying to use combinations
"""

#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    x = sum(arr)
    smallest = x-max(arr)#smallest value will omit largest element
    biggest = x-min(arr) #largest value will omit smallest element
    return(str(smallest)+" "+str(biggest))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    print(miniMaxSum(arr))
