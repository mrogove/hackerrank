"""
https://www.hackerrank.com/challenges/30-regex-patterns/problem
Sample Input

6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output

julia
julia
riya
samantha
tanya


Print an alphabetically-ordered list of first names
for every user with a gmail account.
Each name must be printed on a new line.
"""

#!/bin/python3

import sys

names = [] #init

n = int(input().strip())
for a0 in range(n):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if '@gmail' in emailID:
        names.append(firstName)

names.sort() #alphabetically

for name in names:
    print(name)
