"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

Sample Input

5 6 7
3 6 10

Sample Output

1 1

"""
#!/bin/python3

import sys

def solve(al, bl):
    # Complete this function
    scoreAlice = 0
    scoreBob = 0 #init
    for (a,b) in zip(al,bl):
        if a > b:
            scoreAlice += 1
        elif b > a:
            scoreBob += 1

    return(str(scoreAlice)+" "+str(scoreBob))

#rewrote given to get list (more extensible than three paired variables):
al = list(map(int, input().strip().split()))
bl = list(map(int, input().strip().split()))
result = solve(al, bl)
print(result)
