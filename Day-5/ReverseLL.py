'''***************************************************************

    Following is the class structure of the LinkedListNode class:

    class LinkedListNode
        LinkedListNode(data):
            data = data
            next = None

*****************************************************************'''


def reverseLinkedList(head):
    if (head == None or head.next == None):
        return head
    rest = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return rest
