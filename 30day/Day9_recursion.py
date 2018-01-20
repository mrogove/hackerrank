"""
https://www.hackerrank.com/challenges/30-recursion/problem
Print a single integer denoting N!.

Sample Input

3

Sample Output

6
"""
#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    if n < 2:
        return n
    else:
        return (n*factorial(n-1)) #gets into recursive loop

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
