"""
https://www.hackerrank.com/challenges/making-anagrams/problem
Print a single integer denoting the number of characters
which must be deleted to make the two strings anagrams of each other

e.g.:
Sample Input

cde
abc

Sample Output

4

Methodology borrowed from HR forum user "DomNomNom"

Using Counter means you can compare the abs dif of the two strings.
"""
#!/bin/python3

from collections import Counter

def makingAnagrams(s1, s2):
    # Complete this function
    counts = Counter(s1)
    counts.subtract(s2)
    return(sum(abs(x) for x in counts.values()))#check out counts.values

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
