"""
https://www.hackerrank.com/challenges/30-nested-logic/problemonth


as borrowed from forums, can use tuple comparisons to do this
very cleanly
Sample Input

9 6 2015
6 6 2015

Sample Output

45

on or before: no fine
after day but within same month/year: 15/day
after month but within same year: 500/month
if after calendar year: 10,000 fixed fine

"""
rday, rmonth, ryear = [int(x) for x in input().split(' ')]
eday, emonth, eyear = [int(x) for x in input().split(' ')]

if (ryear, rmonth, rday) <= (eyear, emonth, eday): #inline tuple comparison
    print(0) #no fine
elif (ryear, rmonth) == (eyear, emonth):
    print(15 * (rday - eday)) #if same year/month: go by day
elif ryear == eyear:
    print(500 * (rmonth - emonth)) #elif same year, go by month only
else:
    print(10000) #fixed fine
