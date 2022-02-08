def lengthOfLongestConsecutiveSequence(arr, n):
    h = set(arr)
    ans = 0
    for i in h:
        if i - 1 not in h:
            cnt = 0
            while i in h:
                i += 1
                cnt += 1
            ans = max(cnt, ans)
    return ans
