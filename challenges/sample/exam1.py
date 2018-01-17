"""
pangram has every letter in alphabet
determine if passed string is pangram
"""
#!/bin/python3

import sys
import os

# Complete the function below.
alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
#constraint says all values will be lower case.

print(alphabet)
print(len(alphabet))

def isPangram(strings):
    binString = ''
    #print(strings) #all strings passed in
    i = 0 #init counter

    while i < len(strings):
        compare = list(set(strings[i])) #assign that set
        compare = [c for c in compare if c != ' '] #use list comp to remove space from list

        if len(compare) == len(alphabet): #if no difference between sets
            binString += '1'
        else: #there is some difference
            binString += '0'

        i += 1 #iterate through list

    return(binString)

if __name__ == "__main__":
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    strings_cnt = 0
    strings_cnt = int(input())
    strings_i = 0
    strings = []
    while strings_i < strings_cnt:
        try:
            strings_item = str(input())
        except:
            strings_item = None
        strings.append(strings_item)
        strings_i += 1


    res = isPangram(strings);
    #f.write(res + "\n")
    print(res)

    #f.close()
