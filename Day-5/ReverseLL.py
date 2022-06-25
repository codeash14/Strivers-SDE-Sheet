'''***************************************************************

    Following is the class structure of the LinkedListNode class:

    class LinkedListNode
        LinkedListNode(data):
            data = data
            next = None

*****************************************************************'''

def reverseLinkedList(head):
    # Write your code here.
    newHead=None
    while head!=None:
        temp=head.next
        head.next=newHead
        newHead=head
        head=temp
    return newHead