"""
https://www.hackerrank.com/challenges/30-queues-stacks/problem
"""
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = [] #init lists
        self.queue = [] #init lists

    def pushCharacter(self, c):
        self.stack.append(c) #perform action on list; no need to return.

    def enqueueCharacter(self, c):
        self.queue.insert(0, c) #put in "back" of the queue, [0]

    def popCharacter(self): #takes no args
        return self.stack.pop() #list has pop property that removes last value

    def dequeueCharacter(self):
        return self.queue.pop()

##given and locked:
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
