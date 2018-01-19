"""
pangram has every letter in alphabet
determine if passed string is pangram

1 - strip whitespace from input
2 - use Counter module?
"""
#!/bin/python3

import sys
import os
import string

# Complete the function below.
alphabet = set(string.ascii_lowercase)
#constraint says all values will be lower case.

def isPangram(strings):
    binString = [int(len(list(set(string))) == len(alphabet)) for string in strings]

    return("".join(map(str,binString)))

if __name__ == "__main__":
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    strings_cnt = 0
    strings_cnt = int(input())
    strings_i = 0
    strings = []
    while strings_i < strings_cnt:
        try:
            strings_item = str(input()).replace(" ","") #remove whitespace
        except:
            strings_item = None
        strings.append(strings_item)
        strings_i += 1


    res = isPangram(strings);
    #f.write(res + "\n")
    print(res)

    #f.close()
