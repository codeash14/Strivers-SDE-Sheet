def longestSubSeg(arr, n, k):
    #   Write your code here.
    i, j = 0, 0
    win = float('-inf')
    while i < n:
        if arr[i] == 0:
            k -= 1
        if k < 0:
            if arr[j] == 0:
                k += 1
            j += 1
        i += 1
        win = max(win, (i - j))
    return win
    
    