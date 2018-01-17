"""
https://www.hackerrank.com/challenges/30-review-loop/problem

Given a number and that number of strings,
        print the strings' even-indexed characters
        , followed by a space, then odd-indexed characters
assumes no spaces?
"""
import sys

def scramble(strings):
    for x in strings:
        print(x[::2],x[1::2])

n = int(input().strip())

strings = []
i=0

while i < n:
    try:
        strings_item = str(input())
    except:
        strings_item = None
    strings.append(strings_item)
    i += 1

scramble(strings)
