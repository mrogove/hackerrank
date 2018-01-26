"""
https://www.hackerrank.com/challenges/time-conversion/problem

convert input to military time:
Sample Input

07:05:45PM

Sample Output

19:05:45

"""
#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    inp = s.split(':')
    if(inp[2][2] == 'P'):
        if(inp[0][:2] != '12'):
            inp[0] = int(inp[0])+12
    else:
        #print(inp[0][:2])
        if(inp[0][:2] == '12'):
            inp[0] = '00'

    return(str(inp[0])+':'+str(inp[1])+':'+str(inp[2][:2]))

s = input().strip()
result = timeConversion(s)
print(result)
