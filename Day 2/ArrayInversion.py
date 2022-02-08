from sys import stdin


def merge(arr, beg, mid, end):
    inv = 0
    n1 = mid - beg + 1
    n2 = end - mid

    left = [0] * (n1)
    right = [0] * (n2)

    for i in range(0, n1):
        left[i] = arr[beg + i]

    for j in range(0, n2):
        right[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = beg

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv += n1 - i
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    return inv


def mergeSort(arr, beg, end):
    inv = 0
    if beg < end:
        mid = beg + (end - beg) // 2
        inv += mergeSort(arr, beg, mid)
        inv += mergeSort(arr, mid + 1, end)
        inv += merge(arr, beg, mid, end)
    return inv


def getInversions(arr, n):
    # Write your code here.
    return mergeSort(arr, 0, n - 1)


# Taking inpit using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
