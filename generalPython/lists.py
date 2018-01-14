"""
https://www.hackerrank.com/challenges/python-lists/problem

read in commands; perform those commands to a list.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""
if __name__ == '__main__':

    n = int(input())
    l = [] #initialize

    arg_coms = ['insert', 'append', 'remove']

    for i in range(n): #for each element entered...
        row = input().split(' ')
        com = row[0]

        if com in arg_coms:
            args = map(int, row[1:]) #make all args ints via map
            getattr(l, com)(*args) #borrowed this from Dive Into Python

        elif com != 'print':
            eval("l."+com+"()") #banged head against "()" for too long.

        else:
            print(l)
