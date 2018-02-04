"""
https://www.hackerrank.com/challenges/30-binary-trees/problem

perform breadth-first search

Task
A level-order traversal, also known as a breadth-first search,
visits each level of a tree's nodes from left to right, top to bottom.
You are given a pointer, root, pointing to the root of a binary search tree.
Complete the levelOrder function provided in your editor so that it prints
the level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.
"""
import sys

###given:
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
###end given

    def levelOrder(self,root): #Adapted from AbhishekVermalIIT from forums

        queue = [root] if root else [] #if root is True/exists, then queue is list from root, else empty list.

        while queue: #iterate through list...
            node = queue.pop() #If no index specified pop() removes and returns last item in list
            print(node.data, end=" ") #to console, required for

            if node.left: queue.insert(0,node.left) #insert into left queue
            if node.right: queue.insert(0,node.right) #insert into right queue

###given:
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
