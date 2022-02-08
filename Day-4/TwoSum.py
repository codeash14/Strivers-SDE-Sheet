def pairSum(arr, s):
    ans = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                ans.append(sorted([arr[i], arr[j]]))
    return sorted(ans)

