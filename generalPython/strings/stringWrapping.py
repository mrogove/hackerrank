"""
https://www.hackerrank.com/challenges/text-wrap/problem
Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""
import textwrap

def wrap(string, max_width):
    res = textwrap.fill(string,max_width)
    return res

####GIVEN####:
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
