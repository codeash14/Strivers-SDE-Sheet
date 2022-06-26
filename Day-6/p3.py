from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    # Write your code here.
    pre=Node(0)
    pre.next=head
    l=0
    temp=head
    while temp:
        temp=temp.next
        l+=1
    c=0
    temp=pre
    while l>0 and c<n:
        cur=pre.next
        nxt=cur.next
        x=b[c] if b[c]<=l else l
        if x==0:
            c+=1
            continue
        for i in range(x-1):
            cur.next=nxt.next
            nxt.next=pre.next
            pre.next=nxt
            nxt=cur.next
        pre=cur
        l-=b[c]
        c+=1
    return temp.next
        