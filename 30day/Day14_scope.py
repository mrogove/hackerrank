"""
https://www.hackerrank.com/challenges/30-scope/problem

scope

input handling given

Sample Input

3
1 2 5

Sample Output

4

"""

class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code here
    ### func computeDifference called; assigns value to element maximumDifference.
    ### in input section, d is assigned as an object of Difference class. Has that element.
    ### assign to that value the max-min of the list that is passed as input.
    def computeDifference(self):
        self.maximumDifference = (max(self.__elements) - min(self.__elements))
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
