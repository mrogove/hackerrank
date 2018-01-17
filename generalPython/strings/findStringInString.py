"""
https://www.hackerrank.com/challenges/find-a-string/problem

given an ascii string
, how many times does a second substring appear?

1<=len(string)<=200
"""

def count_substring(string, sub_string):
    count=0
    i=0
    while i<len(string):
        if string.find(sub_string,i)>=0: #returns next index it appears
            i=string.find(sub_string,i)+1 #jump over that index and continue loop
            count+=1
        else:
            break

    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
