"""
https://www.hackerrank.com/challenges/swap-case/problem

You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

0 < len(S) <=1000
print modified string.

Sample Input

HackerRank.com presents "Pythonist 2".

Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

#can use built-in string functionality:
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
