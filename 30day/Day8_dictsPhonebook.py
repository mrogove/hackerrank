"""
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/forum
Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output

sam=99912222
Not found
harry=12299933

create phonebook using dict
"""

n = int(input().strip())
phonebook = {} #a method to turn list to set

#print(phonebook)

for _ in range(n):
    given = input().split()
    phonebook[given[0]] = given[1] #implicitly adds key and value to dict

while True: #run until break
    try:
        name = input()
        if name in phonebook:
            l = [name,phonebook[name]] #give key and its value
            print('='.join(l)) #output chars joined by delimiter
        else:
            print("Not found")
    except:
        break #end run
