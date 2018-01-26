"""
https://www.hackerrank.com/challenges/30-linked-list/problem

Lots of given input; need to define function that inserts to list.

This is an unsatisfying "challenge"/instruction problem.

Leaving code commented out below, but would prefer this in Class constructor:
   def insert(self,head,data):
        if head is None:
            head = Node(data)
            self.tail = head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head
"""
#given:###################
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
#/end given##############
    def insert(self,head,data):
        if head is None:
            return Node(data)
        current = head
        while current.next != None:
            current = current.next
        current.next = Node(data)
        return head


#given:############################
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
