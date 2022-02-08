def ninjaAndSortedArrays(arr1, arr2, m, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while (j >= 0):
        if (i >= 0 and arr1[i] > arr2[j]):
            arr1[k] = arr1[i]
            k -= 1
            i -= 1
        else:
            arr1[k] = arr2[j]
            k -= 1
            j -= 1
    return arr1
