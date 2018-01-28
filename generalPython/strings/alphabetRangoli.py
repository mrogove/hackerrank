"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

Sample Input

5

Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""
import string

def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase

    for i in range(size - 1,0,-1):
        row = ["-"] * (size * 2 - 1)
        for x in range(0,size - i):
            row[size - 1 - x] = alpha[x + i]
            row[size - 1 + x] = alpha[x + i]
        print("-".join(row))
    #bottom half
    for i in range(0,size):
        row = ["-"] * (size * 2 - 1)
        for x in range(0,size - i):
            row[size - 1 - x] = alpha[x + i]
            row[size - 1 + x] = alpha[x + i]
        print("-".join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
