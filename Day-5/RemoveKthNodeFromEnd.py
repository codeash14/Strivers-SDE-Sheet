class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def removeKthNode(head, k):
    dummy =  Node(-1)
    dummy.next = fast = head
    slow = dummy
    for i in range(k):
        if fast:
            fast=fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    if slow.next == None:
        slow.next = None
    else:
        slow.next = slow.next.next 
    return dummy.next

def build_linkedList(arr):
    head = None
    for i in range(len(arr)):
        if arr[i] == -1:
            break

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new

        else:
            tail.next = new
            tail = tail.next

    return head

# Main Code.
t = int(input().strip())
for i in range(t):
    k = int(input().strip())
    arr = [int(i) for i in input().strip().split()]

    head = build_linkedList(arr)
    res_head = removeKthNode(head, k)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)
