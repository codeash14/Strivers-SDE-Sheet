from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data):

            self.data = data
            self.next = None
                
'''

def rotate(head, k):
    # Write your code here.
    if not head or not head.next:
        return head
    temp=head
    l=1
    while temp.next:
        temp=temp.next
        l+=1
    if k==0 or k==l:
        return head
    temp.next=head
    for i in range((l-k)%l):
        temp=temp.next
    head=temp.next
    temp.next=None
 
    return head
    
    