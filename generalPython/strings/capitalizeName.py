"""
https://www.hackerrank.com/challenges/capitalize/problem
Given a full name, your task is to capitalize the name appropriately.

Sample Input

chris alan

Sample Output

Chris Alan
"""
#trivial in python:
def capitalize(string):
    return string.title()


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
