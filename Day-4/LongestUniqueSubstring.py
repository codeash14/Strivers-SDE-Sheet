def uniqueSubstrings(s):
    d = {}
    ans = l = r = 0
    while r < len(s):
        if s[r] in d:
            l = max(l, d[s[r]] + 1)
        d[s[r]] = r
        ans = max(ans, r - l + 1)
        r += 1
    return ans
