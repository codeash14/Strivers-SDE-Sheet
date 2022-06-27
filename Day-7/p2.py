from os import *
from sys import *
from collections import *
from math import *

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        

def cloneRandomList(head):
    hmap = {None: None}
    temp = head
    while temp:
        hmap[temp] = LinkedListNode(temp.data)
        temp = temp.next
    temp = head
    while temp:
        hmap[temp].next = hmap[temp.next]
        hmap[temp].random = hmap[temp.random]
        temp = temp.next

    return hmap[head]
