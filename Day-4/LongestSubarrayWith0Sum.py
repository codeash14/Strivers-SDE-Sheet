def LongestSubsetWithZeroSum(arr):
    #Code here
    s = 0
    d = {}
    mx = 0
    for i in range(len(arr)):
        s += arr[i]
        if s == 0:
            mx = max(mx, i + 1)
        elif s not in d:
            d[s] = i
        else:
            mx = max(mx, i - d[s])
    return mx
