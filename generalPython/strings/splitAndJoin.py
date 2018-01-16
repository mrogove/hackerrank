"""
https://www.hackerrank.com/challenges/python-string-split-and-join/problem
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


Sample Input

this is a string

Sample Output

this-is-a-string


"""
def split_and_join(line):
    # write your code here
    a = line.split() #this splits on spaces by default
    b = "-".join(a) #rejoin
    return(b) #return the rejoin

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
