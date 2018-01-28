"""
https://www.hackerrank.com/challenges/30-more-exceptions/problem
Sample Input

4
3 5
2 4
-1 -2
-1 3

Sample Output

243
16
n and p should be non-negative
n and p should be non-negative
"""
#custom class ,"r", defining an exception
class r(Exception):
    def __init__(self): #default method?
        Exception.__init__(self,"n and p should be non-negative") #will need to read more about this convention

class Calculator:
    def power(self,n,p): #required method from given code
        if n < 0 or p < 0:
            raise r #raise exception 
        else:
            return n**p


####GIVEN####
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
