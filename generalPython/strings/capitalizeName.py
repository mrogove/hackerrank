"""
https://www.hackerrank.com/challenges/capitalize/problem
Given a full name, your task is to capitalize the name appropriately.

Sample Input

chris alan

Sample Output

Chris Alan
"""
import string
#trivial in python:
def capitalize(s):
    t = s.split()
    l = []
    for x in t:
        l.append(x.capitalize())

    return ' '.join(l)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
