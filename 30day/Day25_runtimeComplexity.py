"""
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
The first line contains an integer, , the number of test cases.
Each of the subsequent lines contains an integer, , to be tested for primality.

Sample Input

3
12
5
7

Sample Output

Not prime
Prime
Prime
"""
import math

def check_prime(num):
    if num == 1:
        return "Not prime"
    if num == 2:
        return "Prime"
    if num%2 == 0 :
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(3, sq+1, 2): #increment by 2, as /2 case has already been cleared
        if num % x == 0:
            return "Not prime"
    return "Prime"

T=int(input())
for _ in range(T):
    n=int(input())
    print(check_prime(n))
