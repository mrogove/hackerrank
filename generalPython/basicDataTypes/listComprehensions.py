"""
https://www.hackerrank.com/challenges/list-comprehensions/problem

Given X,Y,Z and N:
X,Y,Z represent dimensions of cuboid.
N is an int.
Print list of all possible (i,j,k) coordinates on a grid
    where sum of i+j+k != N.

Assume 0<=i<=X;0<=j<=Y;0<=k<=Z.

Constraints:
input will always be:
X
Y
Z
N

and crucially: print in lexicographic increasing order!
"""

if __name__ == '__main__':
    x,y,z,n = (int(input()) for x in range(4))

    listOfLists = [[i,j,k] for i in range(x+1)
                           for j in range(y+1)
                           for k in range(z+1)
                           if ((i+j+k) != n)]

    print(listOfLists)
