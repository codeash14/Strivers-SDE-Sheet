from os import *
from sys import *
from collections import *
from math import *

'''
    class Node :
        def __init__(self, data) :
            self.data = data
            self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    visited={}
    while head:
        if head in visited:
            return True
        visited[head]=True
        head=head.next
    return False
    