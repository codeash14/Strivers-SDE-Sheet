def mergeSort(arr, beg, end):
    if beg >= end:
        return 0
    mid = (beg + end) // 2
    count = mergeSort(arr, beg, mid) + mergeSort(arr, mid + 1, end)
    j = mid + 1
    for i in range(beg, mid + 1):
        while j <= end and arr[i] > 2 * arr[j]:
            j += 1
        count += j - mid - 1
    arr[beg:end + 1] = sorted(arr[beg:end + 1])
    return count


def reversePairs(arr, n):
    return mergeSort(arr, 0, len(arr) - 1)
