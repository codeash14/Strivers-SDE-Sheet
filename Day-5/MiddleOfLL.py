'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    nxt=head
    while head and head.next:
        nxt,head=nxt.next,head.next.next
    return nxt
    '''
    l=0
    temp=head
    while temp:
        l+=1
        temp=temp.next
    for i in range(l//2):
        head=head.next
    return head
    '''