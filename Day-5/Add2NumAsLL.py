# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(head1, head2):
    dummy = Node(0)
    cur = dummy
    carry = 0
    while head1 or head2 or carry:
        v1 = head1.data if head1 else 0
        v2 = head2.data if head2 else 0  
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = Node(val)   
        cur = cur.next
        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None
    return dummy.next