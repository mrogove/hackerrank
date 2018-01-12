# https://www.hackerrank.com/challenges/python-tuples/problem

"""
Given an integer, n, and n space-separated integers as input,
create a tuple, t, of those integers.
Then compute and print the result of hash(t)
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #map used to turn into list of ints

    t = tuple(integer_list)
    print(hash(t))
