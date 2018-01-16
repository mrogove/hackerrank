"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array of integers each separated by a space.
Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

plan: input().split() each value (and make int)
        turn into sorted set
        return [1]
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    s = set(arr) #this will dedupe
    l = list(map(int, s)) #makes list again; makes ints
    l.sort() #sorts the list
    print(l[-2]) #prints penultimate value
