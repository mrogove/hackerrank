"""
https://www.hackerrank.com/challenges/30-sorting/problem

Print the following three lines of output:

    Array is sorted in numSwaps swaps.
    where numSwaps is the number of swaps that took place.
    First Element: firstElement
    where firstElement is the first element in the sorted array.
    Last Element: lastElement
    where lastElement is the last element in the sorted array.

opted for script, no funcs
"""
#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swapCount = 0
isSorted = False

while not isSorted: #wrap the whole thing until sorted
    isSorted = True #until otherwise...
    i = 0 #reset
    for i in range(0, len(a)):
        if i < len(a) - 1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                isSorted = False #this run is not sorted. yet.
                swapCount += 1

print('Array is sorted in {} swaps.'.format(swapCount))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
