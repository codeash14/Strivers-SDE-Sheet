from os import *
from sys import *
from collections import *
from math import *

#    List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if (self.next):
            del self.next


def firstNode(head):
    entry=slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            while entry!=slow:
                entry=entry.next
                slow=slow.next
            return slow
    return None
    
        