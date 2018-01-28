"""
https://www.hackerrank.com/challenges/python-string-formatting/problem
Given an integer, n, print the following values for each integer from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary

Sample Input

17

Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

"""
def print_formatted(number):
    # your code goes here
    w = len(str(bin(number))[2:])
    for i in range(1,number+1): #start at 1, go to n+1
        print('{:>{width}}'.format(int(i),width=w),end=" ")
        print('{:>{width}}'.format(str(oct(i))[2:],width=w),end=" ") #octal value
        print('{:>{width}}'.format(str(hex(i))[2:].upper(),width=w),end=" ") #hexvalue
        print('{:>{width}}'.format(str(bin(i))[2:],width=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#after solving this, I came to learn that the .format function could have
#done the reformatting for hex, binary, oct, etc. on its own! cool.
