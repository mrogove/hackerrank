"""
https://www.hackerrank.com/challenges/staircase/problem
Sample Input

6

Sample Output

     #
    ##
   ###
  ####
 #####
######

note: RIGHT ALIGNED
"""
#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    i = 0
    j = n
    for i in range(n):
        print(" "*(j-1),end="") ##need to not terminate as newline; continue with:
        print("#"*(i+1))
        j -= 1

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
