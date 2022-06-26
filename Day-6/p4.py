from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    if not head or not head.next:
        return True
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    cur=slow.next
    pre=None
    nxt=None
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    slow.next=pre
    cp1=head
    cp2=slow.next
    while cp2:
        if cp1.data!=cp2.data:
            return False
        cp1=cp1.next
        cp2=cp2.next
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
