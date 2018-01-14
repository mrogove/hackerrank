"""
https://www.hackerrank.com/challenges/python-lists/problem

read in commands; perform those commands to a list.
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
    #
    # if command=="insert":
    #     l.insert(i,e)
    # elif command=="remove":
    #     l.remove(e)
    # elif command=="append":
    #     l.append(e)
    # elif command=="sort":
    #     l.sort()
    # elif command=="pop":
    #     l.pop()
    # elif command=="reverse":
    #     l.reverse()
    # elif command=="print":
    #     print(l)
