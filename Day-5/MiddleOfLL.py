'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''


def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    nxt = head
    while head and head.next:
        nxt, head = nxt.next, head.next.next
    return nxt
