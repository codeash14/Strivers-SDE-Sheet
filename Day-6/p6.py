from os import *
from sys import *
from collections import *
from math import *

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next
            
def merge(x,y):
    if not x or not y:
        return x or y
    if x.data<y.data:
        res=x
        res.child=merge(x.child,y)
    else:
        res=y
        res.child=merge(x,y.child)
    res.next=None
    return res

def flattenLinkedList(head):
    if not head or not head.next:
        return head
    return merge(head,flattenLinkedList(head.next))
            