"""

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.
https://www.hackerrank.com/challenges/most-commons/problem

Borrowed from: https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/
"""
#example input: aabbbccde
#!/bin/python3

import sys
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
	pass

if __name__ == "__main__":
    s = input().strip()
    mylist = OrderedCounter(sorted(s)).most_common(3)
    for i in mylist:
        print(*i) #prints each dict value with spaces.
    #note that sorted() makes alphabetical
    #OrderedCounter class created from Counter, OrderedDict
