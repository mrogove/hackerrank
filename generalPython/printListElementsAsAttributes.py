"""Given N:
Without using any string methods, try to print the following:
123...N
https://www.hackerrank.com/challenges/python-print/problem
"""

if __name__ == '__main__':
    n = int(input())

    i = 1 #input dictate to start at 1
    newList = []

    while i <= n:
        newList.append(i)
        i += 1

    print(''.join(str(x) for x in newList)) #print list no spaces
