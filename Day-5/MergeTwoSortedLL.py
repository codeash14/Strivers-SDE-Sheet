import sys
from sys import stdin


# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortTwoLists(list1,list2):
    # Write your code here.
    cur = dummy = Node(0)
    while list1 and list2:               
        if list1.data < list2.data:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def ll(arr):

    if len(arr) == 0:
        return None

    head = Node(arr[0])
    last = head

    for data in arr[1:]:

        last.next = Node(data)
        last = last.next

    return head


def printll(head):

    while head:

        print(head.data, end=' ')

        head = head.next

    print(-1)


t = int(sys.stdin.readline().strip())

for i in range(t):

    arr1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))

    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])

    l = sortTwoLists(l1, l2)

    printll(l)
