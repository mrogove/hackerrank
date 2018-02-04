"""
https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

Output Format

Your removeDuplicates function should return the head of the updated linked list.
The locked stub code in your editor will print the returned list to stdout.

Sample Input

6
1
2
2
3
3
4

Sample Output

1 2 3 4

The data elements of the linked list argument will always be in non-decreasing order.
"""
###given:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
###end given

    def removeDuplicates(self,head):
        #Write your code here
        if not head: #if empty...
            return head
        #else:
        nodes = {head.data} #start set based on head.data
        current = head
        while current.next: #while going through list
            if current.next.data not in nodes: #not super efficient; scans set each time
                nodes.add(current.next.data) #adding to set!
                current = current.next #move through list
            elif current.next.data in nodes:
                current.next = current.next.next #move through the list
        return head #got this from forums - not totally sure why not returning manipulation of nodes
                    #all operations on 'nodes' ~have~ been manipulating head linkedlist

###given input handling:
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
